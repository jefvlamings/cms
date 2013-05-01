from django.conf.urls import patterns, url
from pages.views import PagesIndexView, PagesDetailView

# Routing
urlpatterns = patterns('',

    # Any string should redirect to 'detail'
    url(r'(?P<path>.+)$', PagesDetailView.as_view()),

    # An empty string ^$ should redirect to 'index'
    url(r'^$', PagesIndexView.as_view()),

)