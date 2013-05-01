from django.conf.urls import patterns, include, url
from media.views import *
from pages.views import *
import views

# Routing
urlpatterns = patterns(
    '',
    url(r'^/unpublish/(?P<pk>\d+)$', PagesUnpublishView.as_view()),
    url(r'^/publish/(?P<pk>\d+)$', PagesPublishView.as_view()),
    url(r'^/delete/(?P<pk>\d+)$', PagesDeleteView.as_view()),
    url(r'^/edit/(?P<pk>\d+)$', PagesUpdateView.as_view(), name="page-edit"),
    url(r'^/new$', PagesCreateView.as_view()),
    url(r'^/media/delete/(?P<pk>\d+)$', MediaDeleteView.as_view()),
    url(r'^/media/$', MediaCreateView.as_view()),
    url(r'^$', views.index, name='index'),
)