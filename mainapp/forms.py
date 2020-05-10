from django.forms import ModelForm
from django.utils.datastructures import MultiValueDictKeyError

from mainapp.models import Sign


class SignCreateForm(ModelForm):
    data_url = '/sign-form-data/'

    class Meta:
        model = Sign
        fields = ['country', 'region', 'area', 'quality_mark', 'name']

    fields_list = ['country', 'region', 'area', 'quality_mark', 'name']

    class Media:
        js = ('js/form.js',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        num = 0
        attrs_dict = {'onchange': 'addForm(this)', 'class': 'form-control', 'data-url': self.data_url}
        for field_name, field in self.fields.items():
            num += 1
            self.fields[field_name].widget.attrs.update(attrs_dict)
            self.fields[field_name].widget.attrs.update({'num': num})

        parent, child_fields = self.fields_list[0], self.fields_list[1:]
        if self.data:
            try:
                self.prefix = self.data['field_name'][:len(self.data['field_name']) - len(self.Meta.fields[int(self.data['num']) - 1])]
            except MultiValueDictKeyError:
                self.prefix = ''
            print(self.prefix)
            for item in child_fields:  # цикл по 'region', 'area', 'quality_mark', 'name'
                if self.data[self.prefix+parent]:  # если родитель в data имеет данные
                    if 'queryset' in dir(self.fields[item]):  # если поле с queryset-ом (селектовое)
                        for field in self.fields_list[:self.fields_list.index(item)]:  # для полей выше текущего
                            self.fields[item].queryset = self.fields[item].queryset.filter(**{field: self.data[self.prefix+parent]})  # фильтруем кверисет поля по тому, что выбрано в активном поле
                        if len(self.fields[item].queryset) == 0:  # если ничего не выбрано - скрываем все нижние поля
                            for child in self.fields_list[self.fields_list.index(item):]:  # - скрываем все нижние поля
                                self.fields[child].widget.attrs['style'] = 'visibility: hidden'  # - скрываем все нижние поля
                    parent = item
                else:
                    self.fields[item].widget.attrs['style'] = 'visibility: hidden'
            print(self.data)
        else:
            for item in child_fields:
                self.fields[item].widget.attrs['style'] = 'visibility: hidden'
