from django.forms import ModelForm
from django.forms.models import apply_limit_choices_to_to_formfield

from mainapp.models import SignModel


def data_field_match(field_key, form_data):
    """Функция, которая ищет частичное совпадение имени поля в self.data формы
    Поиск происходит с учетом того, что совпадение должно произойти в конце названия поля (которое является ключом словаря self.data)
    Возвращает словарь с названием поля из self.data и префикс к данной форме"""
    match_item = None
    for item, value in form_data.items():
        if field_key in item[-len(field_key):] and len(value) > 0:
            prefix = item[:-len(field_key)]
            match_item = item
            return {'match_item': match_item, 'prefix': prefix}
        elif field_key in item[-len(field_key):]:
            prefix = item[:-len(field_key)]
            return {'match_item': match_item, 'prefix': prefix}
    else:
        return None


class SignCreateForm(ModelForm):
    data_url = '/sign-form-data/'

    class Meta:
        model = SignModel
        #  all fields ancestor class -> django.forms.fields.Field
        fields = ['country', 'region', 'area', 'quality_mark', 'sign']

    fields_list = ['country', 'region', 'area', 'quality_mark', 'sign']
    dependencies = {'quality_mark': ('country', 'region', 'area'), 'area': ('region',), 'region': ('country',)}
    # если меняется значения в select полей country, region или area - должен поменяться список options в select для
    # поля sign. Возможно, что поменяется и значение
    class Media:
        js = ('js/formset.js',)

    def __init__(self, *args, **kwargs):
        parent, child_fields = self.fields_list[0], self.fields_list[1:]
        super().__init__(*args, **kwargs)
        attrs_dict = {'onchange': 'addForm(this)', 'class': 'form-control', 'data-url': self.data_url}
        for field_name, field in self.fields.items():
            self.fields[field_name].widget.attrs.update(attrs_dict)
        if self.is_bound:
            #  заменить на цикл по ключ зависимости - зависимые поля
            #  типа ограничиваем выборку в соответствии с зависимостями

            for key, value in self.dependencies.items():
                prefix = data_field_match(key, self.data)['prefix']
                if len(value) == 1:
                    print(f'{key}, {value}')
                    self.fields[key].limit_choices_to = {value: self.data[prefix+value[0]]}
                else:
                    for i in range(len(value)):
                        print(f'key = {key}, value(s) = {value[i - 1]}, values length = {len(value)}')
                        self.fields[key].limit_choices_to = {value: self.data[prefix + value[i-1]]}


            # for item in child_fields:
            #         if data_field_match(parent, self.data):  # если есть данные в первом поле
            #             prefix = data_field_match(parent, self.data)['prefix']
            #             if self.data[prefix+item]:
            #                 upper_field = self.fields_list[self.fields_list.index(item) - 1]
            #                 self.fields[item].limit_choices_to = {upper_field: self.data[prefix+upper_field]}
            #                 apply_limit_choices_to_to_formfield(self.fields[item])
            #                 parent = item
            #         else:
            #             self.fields[item].widget.attrs['style'] = 'visibility: hidden'
        else:
            for item in child_fields:
                pass
                self.fields[item].widget.attrs['style'] = 'visibility: hidden'
