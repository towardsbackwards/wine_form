import os

from django.forms import formset_factory, BaseFormSet
from django.http import JsonResponse
from django.views.generic import CreateView, FormView, UpdateView
from mainapp.forms import SignCreateForm
from mainapp.models import SignModel
from wine_form_new.settings import STATIC_URL


class ViewJS(FormView):
    """Class for AJAX form transmitting.
    form.errors.clear() is needed because form sends to server every time the user changes any field
    and empty fields may not be allowed by form model. So form.errors.clear() helps JS to avoid empty field errors."""
    form_class = SignCreateForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super(ViewJS, self).form_valid(form)

    def form_invalid(self, form):
        [print(item) for item in form.errors.items()]
        form.errors.clear()
        return JsonResponse({'form': str(form)})


class SignCreateView(FormView):
    # success_url = reverse_lazy('main:Index')
    """Generic class for Country creation form rendering"""
    template_name = "index.html"
    form_class = SignCreateForm
    success_url = '/'


class SignFormset(CreateView):
    model = SignModel
    template_name = "formset.html"
    fields = '__all__'
    success_url = '/'

    def __init__(self, *args, **kwargs):
        super(SignFormset, self).__init__(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        formset = formset_factory(form=SignCreateForm, formset=BaseFormSet, extra=3, can_delete=False, can_order=False)
        context['formset'] = formset
        return context
