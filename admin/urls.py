from django.conf.urls import patterns, include, url
from fileupload.views import FileCreateView, FileDeleteView
import views

# Routing
urlpatterns = patterns(
    '',
    url(r'^/unpublish/(?P<page_id>.+)$', views.unpublish, name='unpublish'),
    url(r'^/publish/(?P<page_id>.+)$', views.publish, name='publish'),
    url(r'^/delete/(?P<page_id>.+)$', views.delete, name='delete'),
    url(r'^/edit/(?P<page_id>.+)$', views.edit, name='edit'),
    url(r'^/media/new/$', FileCreateView.as_view(), {}, 'upload-new'),
    url(r'^/media/delete/(?P<pk>\d+)$', FileDeleteView.as_view(), {}, 'upload-delete'),
    url(r'^/new$', views.edit, name='new'),
    url(r'^$', views.index, name='index'),
)