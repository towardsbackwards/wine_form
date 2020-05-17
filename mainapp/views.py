import os

from django.forms import formset_factory, BaseFormSet
from django.http import JsonResponse
from django.views.generic import CreateView, FormView, UpdateView
from mainapp.forms import SignCreateForm
from mainapp.models import SignModel
from wine_form_new.settings import STATIC_URL


class ViewJS(FormView):
    form_class = SignCreateForm

    def form_valid(self, form):
        super().form_valid(form)
        return JsonResponse({'form': str(form)})

    def form_invalid(self, form):
        super().form_invalid(form)
        form.errors.clear()
        return JsonResponse({'form': str(form)})


class SignCreateView(CreateView):
    # success_url = reverse_lazy('main:Index')
    """Generic class for Country creation form rendering"""
    template_name = "index.html"
    form_class = SignCreateForm
    success_url = '/'


class SignFormset(CreateView):
    model = SignModel
    template_name = "formset.html"
    fields = '__all__'
#
#     def __init__(self, *args, **kwargs):
#         super(SignFormset, self).__init__(*args, **kwargs)
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data()
#         formset = formset_factory(form=SignCreateForm, formset=BaseFormSet, extra=3, can_delete=False, can_order=False)
#         context['formset'] = formset
#         context['form.media'] = os.path.join(STATIC_URL, 'js/formset.js')
#         return context
