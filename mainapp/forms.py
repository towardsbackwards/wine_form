from django.forms import ModelForm

from mainapp.models import Sign, Region


class CountryCreateForm(ModelForm):
    data_url = '/country-form-data/'
    dep_fields = '__all__'

    class Meta:
        model = Sign
        fields = ['country', 'region']
        exclude = ['name',]

    class Media:
        js = ('js/form.js',)

    def __init__(self, *args, **kwargs):
        print('--------------INIT--------------')
        super().__init__(*args, **kwargs)
        attrs_dict = {'onchange': 'addForm(this)', 'style': 'display:', 'data-url': f'{self.data_url}'}
        number = 0
        fields_numerated = {}  # словарь "порядковый номер - имя поля"
        for field_name, field in self.fields.items():
            number += 1
            fields_numerated[number] = field_name  # создали словарь "порядковый номер - имя поля"
            field.widget.attrs['id'] = number  # присваиваем ко всем полям формы цифровые id в порядке возрастания
            widget = self.fields[fields_numerated[number]].widget
            widget.attrs.update(attrs_dict)
            field.widget.attrs['class'] = 'form-control'
            # widget = widget.widget if hasattr(widget, 'widget') else widget

        if self.data:
            active_field = fields_numerated[int(self.data['field_id'])]
            selected_option = self.data[fields_numerated[int(self.data['field_id'])]]
            try:
                current_child = fields_numerated[int(self.data['field_id']) + 1]
            except KeyError:
                current_child = None
            try:
                current_parent = fields_numerated[int(self.data['field_id']) - 1]
            except KeyError:
                current_parent = None

            if len(selected_option) > 0:
                active_field_value = self.fields[active_field].queryset.filter(id=self.data[active_field])
                self.fields[active_field].queryset = active_field_value
            # breakpoint()
            elif len(selected_option) == 0:
                pass
            elif len(selected_option) == 0 and current_parent:
                current_parent

            if current_child and 'queryset' in dir(self.fields[current_child]):
                child_values = self.fields[current_child].queryset.filter(**{active_field: self.data[active_field]})
                self.fields[current_child].queryset = child_values
            for field_name, field in self.fields.items():
                if field.widget.attrs['id'] > int(self.data['field_id']) + 1:
                    field.widget.attrs['style'] = 'display: none'
                    field.label = ''
            # breakpoint()
            # self.data._mutable = True
            # self.data.pop('field_id')
        else:
            # стирание остальных полей
            for field_name, field in self.fields.items():
                if field.widget.attrs['id'] > 1:
                    field.widget.attrs['style'] = 'display: none'
                    field.label = None
        # Подумай как оставить одно поле страну видимым а остальные не видимые

    def save(self, commit=True):
        super().save(commit=True)
        pass


class RegionForm(ModelForm):

    class Meta:
        model = Region
        fields = ('country', 'name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            # number += 1
            field.widget.attrs['class'] = 'form-control'


class SignForm(ModelForm):

    class Meta:
        model = Sign
        fields = ('country', 'region', 'name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            # number += 1
            field.widget.attrs['class'] = 'form-control'