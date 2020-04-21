from django.forms import ModelForm

from mainapp.models import Sign, Region


class CountryCreateForm(ModelForm):
    data_url = '/country-form-data/'
    dep_fields = '__all__'

    class Meta:
        model = Sign
        fields = '__all__'

    class Media:
        js = ('js/form.js',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        attrs_dict = {'onchange': 'addForm(this)', 'style': 'display:', 'data-url': f'{self.data_url}'}
        number = 0
        fields_numerated = {}  # словарь "порядковый номер - имя поля"
        for field_name, field in self.fields.items():
            number += 1
            fields_numerated[number] = field_name  # создали словарь "порядковый номер - имя поля"
            field.widget.attrs['id'] = number  # присваиваем ко всем полям формы цифровые id в порядке возрастания
            widget = self.fields[fields_numerated[number]].widget
            field.widget.attrs['class'] = 'form-control'
            # widget = widget.widget if hasattr(widget, 'widget') else widget
            widget.attrs.update(attrs_dict)
        if self.data:
            # получаем родительское и дочернее поля по соответствию полученного
            # id с id из словаря. решение универсальное для модели с любыми полями и их количеством
            current_parent = fields_numerated[int(self.data['field_id'])]
            try:
                current_child = fields_numerated[int(self.data['field_id']) + 1]
            except KeyError:
                current_child = None
            # breakpoint()
            # подгрузка только следующего поля:
            for field_name, field in self.fields.items():
                # breakpoint()
                if current_child:
                    print(self.fields[current_child].queryset.filter(**{current_parent: self.data[current_parent]}))
                # сравнение присвоенных id-шников с полученным от пользователя
                # если номер поля > номера поля из self.data + 1, то его скрыть
                # т.е. при выбранном поле с id=1, если след. поле (и остальные) > 2, то их скрыть
                if field.widget.attrs['id'] > int(self.data['field_id']) + 1:
                    field.widget.attrs['style'] = 'display: none'
                    field.label = ''
        # Тут вся логика отображения полей, когда передаются данные
        else:
            # стирание остальных полей
            for field_name, field in self.fields.items():
                if field.widget.attrs['id'] > 1:
                    field.widget.attrs['style'] = 'display: none'
                    field.label = ''
        # Подумай как оставить одно поле страну видимым а остальные не видимые


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