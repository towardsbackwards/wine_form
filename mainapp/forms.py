from django.forms import ModelForm

from mainapp.models import Sign, Region


class CountryCreateForm(ModelForm):
    data_url = '/country-form-data/'

    class Meta:
        model = Sign
        fields = '__all__'

    class Media:
        js = ('js/form.js',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # breakpoint()
        print(self.data)
        attrs_dict = {'onchange': 'addForm(this);', 'style': 'display:', 'data-url': f'{self.data_url}'}
        widget = self.fields['country'].widget
        widget = widget.widget if hasattr(widget, 'widget') else widget
        widget.attrs.update(attrs_dict)
        # breakpoint()
        number = 0
        for field_name, field in self.fields.items():
            number += 1
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['id'] = f'form_field_num_{number}'
        # breakpoint()


class RegionForm(ModelForm):

    class Meta:
        model = Region
        fields = ('__all__')
