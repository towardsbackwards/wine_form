from django.forms import ModelForm

from mainapp.models import Sign, Region


class CountryCreateForm(ModelForm):
    data_url = '/country-form-data/'
    dep_fields = ['country', 'region', 'area']
    # saved_data = current_field_name = field_value = current_field_num = None

    class Meta:
        model = Sign
        fields = ['country', 'region', 'area']
        # exclude = ['name', ]

    class Media:
        js = ('js/form.js',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        parent, child_fields = self.dep_fields[0], self.dep_fields[1:]
        attrs_dict = {'onchange': 'addForm(this)', 'style': 'display:', 'data-url': f'{self.data_url}'}
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            self.fields[field_name].widget.attrs.update(attrs_dict)
        if self.data:
            for item in child_fields:
                if self.data[parent]:
                    self.fields[item].queryset = self.fields[item].queryset.filter(**{parent: self.data[parent]})
                    if self.fields[item].queryset.count():  # ???
                        self.fields[item].widget.attrs.update({'style': 'visibility: visible'})
                if self.fields[item].queryset.count(): #???
                    if self.fields[item].queryset.count():
                        self.fields[item].widget.attrs.update({'style': 'visibility: visible'})
                if self.fields[item]:
                    parent = item
                else:
                    self.fields[item].widget.attrs.update({'style': 'visibility: hidden'})
        else:
            for item in child_fields:
                self.fields[item].widget.attrs['style'] = 'visibility: hidden'

    #     print('--------------INIT--------------')
    #     super().__init__(*args, **kwargs)
    #     attrs_dict = {'onchange': 'addForm(this)', 'style': 'display:', 'data-url': f'{self.data_url}'}
    #     number = 0
    #     fields_numerated = {}  # словарь "порядковый номер - имя поля"
    #     for field_name, field in self.fields.items():
    #         number += 1
    #         fields_numerated[number] = field_name  # создали словарь "порядковый номер - имя поля"
    #         field.widget.attrs['id'] = number  # присваиваем ко всем полям формы цифровые id в порядке возрастания
    #         widget = self.fields[fields_numerated[number]].widget
    #         widget.attrs.update(attrs_dict)
    #         field.widget.attrs['class'] = 'form-control'
    #         # widget = widget.widget if hasattr(widget, 'widget') else widget
    #
    #     if self.data:
    #         index = active_field = selected_option = ['']
    #         for key, value in self.data.items():
    #             """Определяем активное поле как "поле со значением перед полем без значения"""
    #             #  добавить "если последнее заполненное = активное"
    #             if value != '':
    #                 print(self.data)
    #                 for s_key, s_value in fields_numerated.items():
    #                     if key == s_value:
    #                         index = s_key
    #                         active_field = s_value
    #                         selected_option = value
    #         print(f'index - {index}, active_field - {active_field}, selected_option - {selected_option} ')
    #         try:
    #             current_child = fields_numerated[index + 1]
    #         except KeyError:
    #             current_child = None
    #         try:
    #             current_parent = fields_numerated[index - 1]
    #         except KeyError:
    #             current_parent = None
    #         for i in range(1, index):
    #             #  цикл очистки полей от лишних значений над текущим полем после каждого выбора
    #             self.fields[fields_numerated[i]].queryset = self.fields[fields_numerated[i]].queryset.filter(id=self.data[fields_numerated[i]])
    #
    #         if len(selected_option) > 0 and self.fields[active_field].widget.input_type == 'select':
    #             # фильтр текущего поля по значениям родителя
    #             pass
    #         if selected_option == '':
    #             for i in range(index, len(fields_numerated) + 1):
    #                 #  цикл очистки полей от лишних значений над текущим полем после каждого выбора
    #                 self.fields[fields_numerated[i]].queryset = self.fields[fields_numerated[i]].queryset.filter(
    #                     id=self.data[fields_numerated[i]])
    #
    #         if current_child and 'queryset' in dir(self.fields[current_child]):
    #             #  фильтр дочернего поля по значению
    #             self.fields[current_child].queryset = self.fields[current_child].queryset.filter(**{active_field: self.data[active_field]})
    #         for field_name, field in self.fields.items():
    #             if field.widget.attrs['id'] > index + 1:
    #                 field.widget.attrs['style'] = 'display: none'
    #                 field.label = ''
    #     else:
    #         # стирание остальных полей
    #         for field_name, field in self.fields.items():
    #             if field.widget.attrs['id'] > 1:
    #                 field.widget.attrs['style'] = 'display: none'
    #
    # def save(self, commit=True):
    #     super().save(commit=True)
    #     pass


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
