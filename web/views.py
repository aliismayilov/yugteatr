from django.shortcuts import render, get_object_or_404

from web.models import Page, Language

def index(request, language_slug=None):
	if language_slug:
		current_language = get_object_or_404(Language, name=language_slug)
	else:
		current_language = Language.objects.all()[0]


	context = {
		'parent_pages': Page.objects.filter(parent=None),
		'languages': Language.objects.all(),
		'current_language': current_language,
	}
	return render(request, 'web/index.html', context)
