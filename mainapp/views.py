from django.forms import formset_factory, BaseFormSet
from django.http import JsonResponse
from django.views.generic import CreateView, FormView, UpdateView
from mainapp.forms import SignCreateForm
from mainapp.models import Sign


class ViewJS(FormView):
    form_class = SignCreateForm

    # def post(self, request, *args, **kwargs):
    #     super().post(request, *args, **kwargs)
    #     print(request.POST)
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


class SignCreateView(CreateView):
    # success_url = reverse_lazy('main:Index')
    """Generic class for Country creation form rendering"""
    template_name = "index.html"
    form_class = SignCreateForm
    success_url = '/'


# class MyFormSet(BaseFormSet):
#
#     def __init__(self):
#         super().__init__()
#         # breakpoint()
#         for i in range(self.total_form_count()):
#             print(self.add_prefix(i))



class SignFormset(UpdateView):
    model = Sign
    template_name = "formset.html"
    fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(SignFormset, self).__init__(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        formset = formset_factory(form=SignCreateForm, formset=BaseFormSet, extra=3, can_delete=False, can_order=False)
        context['formset'] = formset
        return context
