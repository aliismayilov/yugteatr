from django.conf.urls import patterns, url
from django.views.generic.base import TemplateView


urlpatterns = patterns('web.views',
	url(r'^(?P<language_slug>[a-z]{2,3})/(?P<page_slug>(\w|-)+)\.html$', 'show_page', name='show_page'),
    url(r'^(?P<language_slug>[a-z]{2,3})$', 'index', name='index'),
    url(r'^$', 'index', name='index'),
)
