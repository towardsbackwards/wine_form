from django.forms import formset_factory, BaseFormSet
from django.http import JsonResponse
from django.views.generic import CreateView, FormView
from mainapp.forms import SignCreateForm
from mainapp.models import SignModel


class ViewJS(FormView):
    """Class for AJAX form transmitting.
    form.errors.clear() is needed because form sends to server every time the user changes any field
    and empty fields may not be allowed by form model. So form.errors.clear() helps JS to avoid empty field errors."""
    form_class = SignCreateForm

    def form_valid(self, form):
        return self.form_invalid(form)

    def form_invalid(self, form):
        [print(item) for item in form.errors.items()]
        form.errors.clear()
        return JsonResponse({'form': str(form),
                             'field': str(form.fields['country'].queryset.values())})


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

    def __init__(self, *args, **kwargs):
        super(SignFormset, self).__init__(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        formset = formset_factory(form=SignCreateForm, formset=BaseFormSet, extra=3, can_delete=False, can_order=False)
        context['formset'] = formset
        return context
