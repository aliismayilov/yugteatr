from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from web.models import Page, Language, Performance

def index(request, language_slug=None):
    if language_slug:
        current_language = get_object_or_404(Language, name=language_slug)
    else:
        current_language = Language.objects.all()[0]

    upcoming_performance = Performance.objects.filter(
        show_time__gte=timezone.now()
    )
    # if there's some get closest, else none
    if upcoming_performance:
        upcoming_performance = upcoming_performance.latest('show_time')
        upcoming_playinformation = upcoming_performance.get_playinformation(current_language)
    else:
        upcoming_performance = None
        upcoming_playinformation = None

    context = {
        'upcoming_performance': upcoming_performance,
        'upcoming_playinformation': upcoming_playinformation,
        'parent_pages': Page.objects.filter(parent=None),
        'languages': Language.objects.all(),
        'current_language': current_language,
    }
    return render(request, 'web/index.html', context)

def show_page(request, language_slug, page_slug):
    if language_slug:
        current_language = get_object_or_404(Language, name=language_slug)
    else:
        current_language = Language.objects.all()[0]

    page = get_object_or_404(Page,
        slug=page_slug,
        language=current_language
    )


    context = {
        'page': page,
        'parent_pages': Page.objects.filter(parent=None),
        'languages': Language.objects.all(),
        'current_language': current_language,
    }
    return render(request, 'web/show_page.html', context)
