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
        # print(self.data)
        attrs_dict = {'onchange': 'addForm(this)', 'style': 'display:', 'data-url': f'{self.data_url}'}

        number = 0
        fields_numerated = {}
        for field_name, field in self.fields.items():
            number += 1
            fields_numerated[number] = field_name # создали словарь "порядковый номер - имя поля"
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['id'] = number  # присваиваем ко всем полям формы цифровые id в порядке возрастания
            widget = self.fields[fields_numerated[number]].widget
            widget = widget.widget if hasattr(widget, 'widget') else widget
            widget.attrs.update(attrs_dict)

        if self.data:
            # подгрузка только следующего поля:
            for field_name, field in self.fields.items():
                if field.widget.attrs['id'] > int(self.data['field_id']) + 1:
                    field.widget.attrs['style'] = 'display: none'
                    # field.label = ''
        # Тут вся логика отображения полей, когда передаются данные
        else:
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