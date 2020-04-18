from django.forms import modelform_factory
from django.http import JsonResponse, Http404
from django.views.generic import CreateView, FormView
from mainapp.forms import CountryCreateForm


class ViewJS(FormView):
    form_class = CountryCreateForm

    def get_form_class(self):
        form_class = super().get_form_class()
        form = modelform_factory(form_class._meta.model, form_class, fields=form_class._meta.fields)
        # breakpoint()
        return form

    def form_valid(self, form):
        return JsonResponse({'form': str(form)})

    def form_invalid(self, form):
        return JsonResponse({'form': str(form)})

    # def post(self, request, *args, **kwargs):
    #     if request.is_ajax():
    #         parent_id = {
    #             'parent number you choose': int(request.POST.get('country')),
    #             'field id you choose': request.POST.get('field_id')
    #         }
    #         print(request.POST)
    #         # items = MODELITEM.objects.filter(parent_id=parent_id).order_by('name')
    #         return JsonResponse(parent_id)
    #     return Http404()


class CountryCreateView(CreateView):
    """Generic class for Country creation form rendering"""
    template_name = "index.html"
    form_class = CountryCreateForm
