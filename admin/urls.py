from django.conf.urls import patterns, url
import views

# Routing
urlpatterns = patterns('',

    # An empty string ^$ should redirect to 'index'
    url(r'^$', views.index, name='index'),

)