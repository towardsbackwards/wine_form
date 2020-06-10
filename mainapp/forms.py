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
    dependencies = {'sign': ('country', 'region', 'area'), 'area': 'region', 'region': 'country'}

    class Media:
        js = ('js/form.js',)

    def __init__(self, *args, **kwargs):
        parent, child_fields = self.fields_list[0], self.fields_list[1:]
        super().__init__(*args, **kwargs)
        attrs_dict = {'onchange': 'addForm(this)', 'class': 'form-control', 'data-url': self.data_url}
        for field_name, field in self.fields.items():
            self.fields[field_name].widget.attrs.update(attrs_dict)
        if self.is_bound:
            for item in child_fields:
                    if data_field_match(parent, self.data):  # если есть данные в первом поле
                        prefix = data_field_match(parent, self.data)['prefix']
                        upper_field = self.fields_list[self.fields_list.index(item) - 1]
                        self.fields[item].limit_choices_to = {upper_field: self.data[prefix+upper_field]}
                        apply_limit_choices_to_to_formfield(self.fields[item])
                        parent = item
                        #  надо ли отделять префикс. для одного парента логика сработает, но как это будет работать для 2 и более парентов?
                        #  подумать тут о переделке на полностью по полям, хз как но над
                    else:
                        self.fields[item].widget.attrs['style'] = 'visibility: hidden'
        else:
            for item in child_fields:
                self.fields[item].widget.attrs['style'] = 'visibility: hidden'
