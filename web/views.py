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
    ).latest('show_time')


    context = {
        'upcoming_performance': upcoming_performance,
        'upcoming_playinformation': upcoming_performance.get_playinformation(current_language),
        'parent_pages': Page.objects.filter(parent=None),
        'languages': Language.objects.all(),
        'current_language': current_language,
    }
    return render(request, 'web/index.html', context)
