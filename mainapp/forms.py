from django.forms import ModelForm
from django.forms.models import apply_limit_choices_to_to_formfield

from mainapp.models import SignModel


def data_field_match(field_key, form_data):
    """Функция, которая ищет частичное совпадение имени поля в self.data формы
    Поиск происходит с учетом того, что совпадение должно произойти в конце названия поля (которое является ключом словаря self.data)
    Возвращает словарь с названием поля из self.data и префикс к данной форме"""
    for item, value in form_data.items():
        if field_key in item[-len(field_key):]: # and len(value) > 0
            prefix = item[:-len(field_key)]
            match_item = item
            return {'full_name': prefix+match_item, 'prefix': prefix}
    else:
        return None


class SignCreateForm(ModelForm):
    data_url = '/sign-form-data/'

    class Meta:
        model = SignModel
        #  all fields ancestor class -> django.forms.fields.Field
        fields = ['country', 'region', 'area', 'quality_mark', 'sign']

    dependencies = {'quality_mark': ('country', 'region', 'area'), 'area': ('region',), 'region': ('country',)}

    class Media:
        js = ('js/formset.js',)

    # def add_prefix(self, field_name):
    #     return f'{self.prefix}{field_name}' if self.prefix else field_name

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        attrs_dict = {'onchange': 'addForm(this)', 'class': 'form-control', 'data-url': self.data_url}
        for field_name, field in self.fields.items():
            self.fields[field_name].widget.attrs.update(attrs_dict)

        if self.is_bound:
            for key, value in self.dependencies.items():
                prefix = data_field_match(key, self.data).get('prefix')
                self.prefix = prefix[:-1]
                #  ставим временный self.prefix для отправляемой по AJAX формы
                #  self.prefix нужно определять по активному полю, а не всем полям в зависимостях

                for item in value:
                    print(key, item)
                    if self.data[prefix+item]:
                        self.fields[key].limit_choices_to = {item: self.data[self.prefix+'-'+item]}
                        apply_limit_choices_to_to_formfield(self.fields[key])
                        print(self.fields[key].queryset)
