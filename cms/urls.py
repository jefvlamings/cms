from django.conf.urls import patterns, include, url
import settings

urlpatterns = patterns(
    '',
    url(r'^admin', include('admin.urls')),
    url(r'^files/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
    url(r'^', include('pages.urls')),
)