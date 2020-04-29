from django.forms import modelform_factory
from django.http import JsonResponse, Http404
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView
from mainapp.forms import CountryCreateForm, RegionForm


class ViewJS(FormView):
    form_class = CountryCreateForm

    def get_form_class(self):
        form_class = super().get_form_class()
        form = modelform_factory(form_class.Meta.model, form_class, fields=form_class._meta.fields)
        return form

    def form_valid(self, form):
        super().form_valid(form)
        return JsonResponse({'form': str(form)})

    def form_invalid(self, form):
        return JsonResponse({'form': str(form)})


class CountryCreateView(CreateView):
    # success_url = reverse_lazy('main:Index')
    """Generic class for Country creation form rendering"""
    template_name = "index.html"
    form_class = CountryCreateForm

    def get_success_url(self):
        return reverse_lazy('main:Index')