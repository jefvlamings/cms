from django.conf.urls import patterns, url
from pages import views

# Routing
urlpatterns = patterns('',

    # Any string should redirect to 'detail'
    url(r'(?P<path>.+)$', views.detail, name='detail'),

    # An empty string ^$ shoud redirect to 'index'
    url(r'^$', views.index, name='index'),

)