from django.conf.urls import patterns, url
import views

# Routing
urlpatterns = patterns('',

    # Anything proceeding 'edit' should go to 'edit'
    url(r'^/edit/(?P<page_id>.+)$', views.edit, name='edit'),

    # An empty string ^$ should redirect to 'index'
    url(r'^$', views.index, name='index'),

)