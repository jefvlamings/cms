from django.conf import settings
from pages.models import Page

# Base processor
def root_pages(request):
    root_pages = Page.objects.filter(parent=None).all()
    return {'root_pages': root_pages}
