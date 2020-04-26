from django.forms import ModelForm

from mainapp.models import Sign, Region


class CountryCreateForm(ModelForm):
    data_url = '/country-form-data/'
    dep_fields = '__all__'
    saved_data = set()

    class Meta:
        model = Sign
        fields = '__all__'
        exclude = ['name', ]

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

            global saved_data
            if self.data:
                try:
                    print(saved_data)
                    field_oid = None
                    for key, value in saved_data.items():
                        if self.data[key] != value:
                            field_fid = key
                            print('FIELD FOR ID', field_fid)
                except NameError:
                    field_oid = 'country'

                saved_data = self.data
                print(self.data)
                print('FRIELD_OID', field_oid)


            current_field_num = int(self.data['field_id'])
            active_field = fields_numerated[current_field_num]
            selected_option = self.data[fields_numerated[current_field_num]]
            try:
                current_child = fields_numerated[current_field_num + 1]
            except KeyError:
                current_child = None
            try:
                current_parent = fields_numerated[current_field_num - 1]
            except KeyError:
                current_parent = None
            if (current_field_num - 2) >= 1:  # if current field index = 3 or higher
                for i in range(1, (
                        current_field_num - 1)):  # in a range of all fields between 0 and current parent (not inclusive)
                    self.fields[fields_numerated[i]].queryset = \
                        self.fields[fields_numerated[i]].queryset.filter(id=self.data[fields_numerated[i]])
                    self.fields[fields_numerated[i]].widget.attrs['readonly'] = True

            if len(selected_option) > 0 and not current_parent:
                print(self.data)
                print('len(selected_option) > 0 and not current_parent')
                active_field_value = self.fields[active_field].queryset.filter(id=self.data[active_field])
                self.fields[active_field].queryset = active_field_value
                self.fields[fields_numerated[current_field_num]].widget.attrs['readonly'] = True

            elif len(selected_option) == 0 and not current_parent:
                self.fields[current_child].widget.attrs['style'] = 'display: none'
                print('len(selected_option) == 0 and not current_parent')

            elif len(selected_option) == 0 and len(current_parent) > 0:
                print('len(selected_option) == 0 and len(current_parent) > 0')
                active_field_value = self.fields[active_field].queryset.filter(id=self.data[current_parent])
                self.fields[active_field].queryset = active_field_value
                self.fields[current_child].widget.attrs['style'] = 'display: none'
                print(f'I HIDE {current_child}')
            elif len(selected_option) > 0 and current_parent:
                print('len(selected_option) > 0 and current_parent')
                current_parent_value = self.fields[current_parent].queryset.filter(id=self.data[active_field])
                active_field_value = self.fields[active_field].queryset.filter(id=self.data[active_field])
                self.fields[current_parent].queryset = current_parent_value
                self.fields[active_field].queryset = active_field_value
                self.fields[active_field].empty_label = None
                self.fields[current_parent].widget.attrs['readonly'] = True
            if current_child and len(selected_option) > 0:
                if 'queryset' in dir(self.fields[current_child]):
                    child_values = self.fields[current_child].queryset.filter(**{active_field: self.data[active_field]})
                    self.fields[current_child].queryset = child_values
            for field_name, field in self.fields.items():
                if field.widget.attrs['id'] > int(self.data['field_id']) + 1:
                    field.widget.attrs['style'] = 'display: none'
                    field.label = ''

            # breakpoint()
            # self.data._mutable = True
            # self.data.pop('field_id')
            # breakpoint()
            # print(f'PARENT - {current_parent}, CHILD - {current_child}, ACTIVE - {active_field}')
        else:
            # стирание остальных полей
            for field_name, field in self.fields.items():
                if field.widget.attrs['id'] > 1:
                    field.widget.attrs['style'] = 'display: none'
                    field.label = None

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
