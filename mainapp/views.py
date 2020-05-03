from django.forms import modelform_factory
from django.http import JsonResponse, Http404
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView
from mainapp.forms import CountryCreateForm


class ViewJS(FormView):
    form_class = CountryCreateForm

    # def post(self, request, *args, **kwargs):
    #     super().post(request, *args, **kwargs)
    #     print(request.POST)
    #     breakpoint()
    #     form = self.get_form()
    #     if form.is_valid():
    #         return self.form_valid(form)
    #     else:
    #         return self.form_invalid(form)

    def form_valid(self, form):
        # super().form_valid(form)
        return self.form_invalid(form)

    def form_invalid(self, form):
        form.errors.clear()
        return JsonResponse({'form': str(form)})


class CountryCreateView(CreateView):
    # success_url = reverse_lazy('main:Index')
    """Generic class for Country creation form rendering"""
    template_name = "index.html"
    form_class = CountryCreateForm
    success_url = '/'
