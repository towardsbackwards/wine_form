import re
from pprint import pprint

from django.forms import BaseFormSet

fields = {'country': '<django.forms.models.ModelChoiceField object at 0x0000024B69ADE3C8>',
          'region': '<django.forms.models.ModelChoiceField object at 0x0000024B69ADE408>',
          'area': '<django.forms.models.ModelChoiceField object at 0x0000024B69ADE4C8>', 'quality_mark':
              '<django.forms.models.ModelChoiceField object at 0x0000024B69ADDF88>',
          'name': '<django.forms.fields.CharField object at 0x0000024B69ADD848>'}

data = {
    'csrfmiddlewaretoken': ['DE8KDzurSDT1X9am16vWUL06yOe3hlhLUspIRtakJuXphhfh6WlgJTm1oG30Tz6k'],
    'form-TOTAL_FORMS': ['3'],
    'form-INITIAL_FORMS': ['0'],
    'form-MIN_NUM_FORMS': ['0'],
    'form-MAX_NUM_FORMS': ['1000'],
    'form-0-country': ['1'],
    'form-0-region': [''],
    'form-0-area': [''],
    'form-0-quality_mark': [''],
    'form-0-name': [''],
    'form-1-country': [''],
    'form-1-region': [''],
    'form-1-area': [''],
    'form-1-quality_mark': [''],
    'form-1-name': [''],
    'form-2-country': [''],
    'form-2-region': [''],
    'form-2-area': [''],
    'form-2-quality_mark': [''],
    'form-2-name': ['']
}

# префикс должен быть верным на момент начала цикла / проверки
# префикс попробовать взять из данных, а не вычислять из разницы словарей
# prefix0 = 'form-0-'
# prefix1 = ''
# print(data[prefix0+'country'])
# print(data[prefix1+'country'])


# class BaseArticleFormSet(BaseFormSet):
#     def get_default_prefix(cls):
#
#
# ArticleFormSet = formset_factory(ArticleForm, formset=BaseArticleFormSet)


# def add_prefix(prefix, index):
#     return '%s-%s' % (prefix, index)
#
#
# print(add_prefix('data', 1))

# chilren_fields = ['form-0-country', 'form-0-region', 'form-0-area', 'form-0-quality_mark', 'form-0-name']
# clean_fields = list(map(lambda x: x.replace(self.prefix, ''), chilren_fields))

key = 'country'
# print(len(data['form-1-country'][0]))


def data_field_match(form_data, field_key):
    """Функция, которая ищет частичное совпадение имени поля в self.data формы
    Поиск происходит с учетом того, что совпадение должно произойти в конце названия поля (которое является ключом словаря self.data)
    Возвращает словарь с названием поля из self.data и префикс к данной форме"""
    match_item = None
    prefix = None
    for item, value in form_data.items():
        if field_key in item and len(value[0]) > 0:
            if field_key in item[-len(field_key):]:
            # учесть, что в ключах может быть все что угодно, добавить проверку на содержание объекта в конце ключа после совпадения
                prefix = item[:-len(field_key)]
                match_item = item
    return {'match_item': match_item, 'prefix': prefix}

#
# print(data_field_match(data, key)['match_item'])


dependencies = {'sign': ('country', 'region', 'area'), 'area': ('region',), 'region': ('country',)}

for key, value in dependencies.items():
    if len(value) == 1:
        print(f'{key}, {value}')
    else:
        for i in range(len(value)):
            print(f'key = {key}, value(s) = {value[i-1]}, values length = {len(value)}')