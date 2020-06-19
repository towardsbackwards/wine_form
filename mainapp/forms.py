from django.core.exceptions import FieldError
from django.forms import ModelForm
from django.forms.models import apply_limit_choices_to_to_formfield

from mainapp.models import SignModel


def data_field_match(field_key, form_data):
    """Функция, которая ищет частичное совпадение имени поля в self.data формы
    Поиск происходит с учетом того, что совпадение должно произойти в конце названия поля (которое является ключом словаря self.data)
    Возвращает словарь с названием поля из self.data и префикс к данной форме"""
    match_item = None
    for item, value in form_data.items():
        if field_key in item[-len(field_key):]: # and len(value) > 0
            prefix = item[:-len(field_key)]
            match_item = item
            return {'match_item': match_item, 'prefix': prefix}
    else:
        return None


class SignCreateForm(ModelForm):
    data_url = '/sign-form-data/'

    class Meta:
        model = SignModel
        #  all fields ancestor class -> django.forms.fields.Field
        fields = ['country', 'region', 'area', 'quality_mark', 'sign']

    dependencies = {'quality_mark': ('country', 'region', 'area'), 'area': ('region',), 'region': ('country',)}
    # если меняется значения в select полей country, region или area - должен поменяться список options в select для
    # поля sign. Возможно, что поменяется и значение

    class Media:
        js = ('js/formset.js',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        attrs_dict = {'onchange': 'addForm(this)', 'class': 'form-control', 'data-url': self.data_url}
        for field_name, field in self.fields.items():
            self.fields[field_name].widget.attrs.update(attrs_dict)
        if self.is_bound:
            #  заменить на цикл по ключ зависимости - зависимые поля
            #  ограничиваем выборку в соответствии с зависимостями
            for field in self.Meta.fields[1:]:
                prefix = data_field_match(field, self.data)['prefix']
                if self.data[prefix+field]:
                    print(f'Printing field with data: {field}')
                    print(field)
                    self.fields[field].limit_choices_to = {'region__country': self.data[prefix+'country']}
                    # self.data.get(self.add_prefix('country'))
                    apply_limit_choices_to_to_formfield(self.fields[field])
                    # self.fields.objects or smth for

    # def _html_output(self,  *args, **kwargs):
    #     super()._html_output(*args, **kwargs)






























                # for key, value in self.dependencies.items():
                #     prefix = data_field_match(key, self.data)['prefix']
                #     #  добавить "если значение выбрано", иначе ошибка пустого ключа для фильтра
                #     if len(value) == 1:
                #         if self.data[prefix+value[0]]:
                #             self.fields[key].limit_choices_to = {value: self.data[prefix+value[0]]}
                #             apply_limit_choices_to_to_formfield(self.fields[key])
                #     elif len(value) > 1:
                #         for i in range(len(value)):
                #             if self.data[prefix + value[i-1]]:
                #                 self.fields[key].limit_choices_to = {value[i-1]: self.data[prefix + value[i-1]]}
                #                 apply_limit_choices_to_to_formfield(self.fields[key])
