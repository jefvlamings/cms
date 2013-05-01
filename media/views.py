from media.models import Media
from django.views.generic import CreateView, DeleteView
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
import json


def response_mimetype(request):
    if "application/json" in request.META['HTTP_ACCEPT']:
        return "application/json"
    else:
        return "text/plain"


# Create
class MediaCreateView(CreateView):
    model = Media
    template_name = "media/index.html"

    def form_valid(self, form):
        self.object = form.save()
        f = self.request.FILES.get('file')
        data = [{
            'name': f.name,
            'url': f.name.replace(" ", "_"),
            'thumbnail_url': f.name.replace(" ", "_"),
            'delete_url': 'admin/media/delete/' + str(self.object.pk),
            'delete_type': "DELETE"
        }]
        response = JSONResponse(data, {}, response_mimetype(self.request))
        response['Content-Disposition'] = 'inline; filename=files.json'
        return response

    def get_context_data(self, **kwargs):
        context = super(MediaCreateView, self).get_context_data(**kwargs)
        context['files'] = Media.objects.all()
        return context


# Delete
class MediaDeleteView(DeleteView):
    model = Media

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        if request.is_ajax():
            response = JSONResponse(True, {}, response_mimetype(self.request))
            response['Content-Disposition'] = 'inline; filename=files.json'
            return response
        else:
            return HttpResponseRedirect('/admin/media/')


# JSON response
class JSONResponse(HttpResponse):
    def __init__(self, obj='', json_opts={}, mimetype="application/json", *args, **kwargs):
        content = json.dumps(obj, **json_opts)
        super(JSONResponse,self).__init__(content, mimetype, *args, **kwargs)
