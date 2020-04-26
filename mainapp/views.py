from django.forms import modelform_factory
from django.http import JsonResponse, Http404
from django.views.generic import CreateView, FormView
from mainapp.forms import CountryCreateForm, RegionForm


class ViewJS(FormView):
    form_class = CountryCreateForm

    # def get_form_class(self):
    #     form_class = super().get_form_class()
    #     # breakpoint()
    #     form = modelform_factory(form_class.Meta.model, form_class, fields=form_class._meta.fields)
    #     # breakpoint()
    #
    #     return form

    def form_valid(self, form):
        # breakpoint()
        return JsonResponse({'form': str(form)})

    def form_invalid(self, form):
        return JsonResponse({'form': str(form)})


class CountryCreateView(CreateView):
    """Generic class for Country creation form rendering"""
    template_name = "index.html"
    form_class = CountryCreateForm

