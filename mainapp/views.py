from django.http import JsonResponse, Http404
from django.views.generic import CreateView, FormView
from mainapp.forms import CountryCreateForm


class ViewJS(FormView):
    form_class = CountryCreateForm

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            data = {'country you chose': str(request.POST)}

            return JsonResponse(data)
        return Http404()


class CountryCreateView(CreateView):
    """Generic class for Country creation form rendering"""
    template_name = "index.html"
    form_class = CountryCreateForm
