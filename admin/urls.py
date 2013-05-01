from django.conf.urls import patterns, include, url
import media.views
import views

# Routing
urlpatterns = patterns(
    '',
    url(r'^/unpublish/(?P<page_id>.+)$', views.unpublish, name='unpublish'),
    url(r'^/publish/(?P<page_id>.+)$', views.publish, name='publish'),
    url(r'^/delete/(?P<page_id>.+)$', views.delete, name='delete'),
    url(r'^/edit/(?P<page_id>.+)$', views.edit, name='edit'),
    url(r'^/media/delete/(?P<pk>\d+)$', media.views.MediaDeleteView.as_view(), {}, 'upload-delete'),
    url(r'^/media/$', media.views.MediaCreateView.as_view(), {}, 'upload-new'),
    url(r'^/new$', views.edit, name='new'),
    url(r'^$', views.index, name='index'),
)