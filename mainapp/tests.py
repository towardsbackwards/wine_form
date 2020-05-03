# data1 = {'csrfmiddlewaretoken': ['cpWuNxH88ZRG3A5ouCdJHKWywL6baFUyeCR7YGpAD9U4TrLhaCR7Td6y0bQU1JfK'], 'country': ['2'], 'region': [''], 'area': [''], 'quality_mark': [''], 'sign': [''], 'field_id': ['1']}
# data2 = {'csrfmiddlewaretoken': ['cpWuNxH88ZRG3A5ouCdJHKWywL6baFUyeCR7YGpAD9U4TrLhaCR7Td6y0bQU1JfK'], 'country': ['1'], 'region': [''], 'area': [''], 'quality_mark': [''], 'sign': [''], 'field_id': ['1']}
#
# # for key, value in data1.items():
# #     if data2[key] != value:
# #         field_id = key
# #     print(data2[key])
# # print(field_id)
# self_data = {'csrfmiddlewaretoken': ['cpWuNxH88ZRG3A5ouCdJHKWywL6baFUyeCR7YGpAD9U4TrLhaCR7Td6y0bQU1JfK'], 'country': ['2'], 'region': ['1'], 'area': [''], 'quality_mark': ['33'], 'sign': ['1231']}
# fields_numerated = {1: 'country', 2: 'region', 3: 'area', 4: 'quality_mark', 5: 'sign'}
#
#
# for key, value in self_data.items():
#     if value != ['']:
#         print(key, value)
#         for s_key, s_value in fields_numerated.items():
#             if key == s_value:
#                 index = s_key
#                 name = s_value
#                 option = value
# print(f'index последнего заполненного поля в форме = {index}, название - {name}, выбрано - {value}')

import itertools as it
import random

fields = ['country', 'region', 'area', 'quality_mark']
new = []
parent = 'area'
print(parent)
asda = fields[:fields.index(parent)]

for item in fields:
    if item != parent:
        new.append(item)
    else:
        break
print(asda)
#new2 = list(it.takewhile(lambda x: x != parent, fields))
#print(new2)
# new3 = []
# [new3.append(field) for field in fields if field != parent]