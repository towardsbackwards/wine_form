from django.forms import ModelForm
# from django import forms
#
from mainapp.models import SignModel


class SignCreateForm(ModelForm):
    data_url = '/sign-form-data/'

    class Meta:
        model = SignModel
        fields = ['country', 'region', 'area', 'quality_mark', 'name']

    fields_list = ['country', 'region', 'area', 'quality_mark', 'name']

    class Media:
        js = ('js/form.js',)
#
#     def add_prefix(self, field_name):
#         super().add_prefix(field_name)
#         return f'{self.prefix}{field_name}' if self.prefix else field_name
#
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        attrs_dict = {'onchange': 'addForm(this)', 'class': 'form-control', 'data-url': self.data_url}
        for field_name, field in self.fields.items():
            self.fields[field_name].widget.attrs.update(attrs_dict)
#
#         parent, child_fields = self.fields_list[0], self.fields_list[1:]
#         if self.is_bound:
#             pass
