import re

from django.forms import BaseFormSet

fields = {'country': '<django.forms.models.ModelChoiceField object at 0x0000024B69ADE3C8>', 'region': '<django.forms.models.ModelChoiceField object at 0x0000024B69ADE408>', 'area': '<django.forms.models.ModelChoiceField object at 0x0000024B69ADE4C8>', 'quality_mark':
    '<django.forms.models.ModelChoiceField object at 0x0000024B69ADDF88>', 'name': '<django.forms.fields.CharField object at 0x0000024B69ADD848>'}

data = {'csrfmiddlewaretoken': ['DE8KDzurSDT1X9am16vWUL06yOe3hlhLUspIRtakJuXphhfh6WlgJTm1oG30Tz6k'], 'form-TOTAL_FORMS': ['3'], 'form-INITIAL_FORMS': ['0'], 'form-MIN_NUM_FORMS': ['0'], 'form-MAX_NUM_FORMS': ['1000'], 'form-0-country': ['1'], 'form-0-region':
[''], 'form-0-area': [''], 'form-0-quality_mark': [''], 'form-0-name': [''], 'form-1-country': [''], 'form-1-region': [''], 'form-1-area': [''], 'form-1-quality_mark': [''], 'form-1-name': [''], 'form-2-country': [''], 'form-2-region': [''], 'form-2-area': [''],
        'form-2-quality_mark': [''], 'form-2-name': ['']}


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

a = 'form-0-my-beautiful-form-country'
b = 'my-beautiful-form-country'
d = a[:len(a) - len(b)]
print(type(d), d)