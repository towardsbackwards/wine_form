data1 = {'csrfmiddlewaretoken': ['cpWuNxH88ZRG3A5ouCdJHKWywL6baFUyeCR7YGpAD9U4TrLhaCR7Td6y0bQU1JfK'], 'country': ['2'], 'region': [''], 'area': [''], 'quality_mark': [''], 'sign': [''], 'field_id': ['1']}
data2 = {'csrfmiddlewaretoken': ['cpWuNxH88ZRG3A5ouCdJHKWywL6baFUyeCR7YGpAD9U4TrLhaCR7Td6y0bQU1JfK'], 'country': ['1'], 'region': [''], 'area': [''], 'quality_mark': [''], 'sign': [''], 'field_id': ['1']}

for key, value in data1.items():
    if data2[key] != value:
        field_id = key
print(field_id)