from django.forms import ModelForm
from mainapp.models import Sign


class CountryCreateForm(ModelForm):
    data_url = '/country-form-data/'
    dep_fields = ['country', 'region', 'area', 'quality_mark', 'name']

    class Meta:
        model = Sign
        fields = ['country', 'region', 'area', 'quality_mark', 'name']

    class Media:
        js = ('js/form.js',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        parent, child_fields = self.dep_fields[0], self.dep_fields[1:]
        attrs_dict = {'onchange': 'addForm(this)', 'class': 'form-control', 'data-url': self.data_url}
        for field_name, field in self.fields.items():
            self.fields[field_name].widget.attrs.update(attrs_dict)
        if self.data:
            for item in child_fields:
                if self.data[parent]:  # если есть данные в первом поле
                    if 'queryset' in dir(self.fields[item]):
                        for field in self.dep_fields[:self.dep_fields.index(item)]:  # мой супир-пупир цикл
                            self.fields[item].queryset = self.fields[item].queryset.filter(**{field: self.data[field]})
                        if len(self.fields[item].queryset) == 0:  # len, а не count() чтобы не обращаться к БД каждый раз
                            for child in self.dep_fields[self.dep_fields.index(item):]:
                                self.fields[child].widget.attrs['style'] = 'visibility: hidden'  # обходит условие наличия 'queryset' и скрывает все поля, ниже item
                    parent = item
                else:
                    self.fields[item].widget.attrs['style'] = 'visibility: hidden'
        else:
            for item in child_fields:
                self.fields[item].widget.attrs['style'] = 'visibility: hidden'
