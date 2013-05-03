from django.conf.urls import patterns, url
from django.views.generic.base import TemplateView


urlpatterns = patterns('web.views',
    url(r'^$', 'index', name='index'),
)
