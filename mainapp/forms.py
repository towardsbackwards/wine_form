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

    def add_prefix(self, field_name):
        return f'{self.prefix}{field_name}' if self.prefix else field_name

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
            self.prefix = self.data['field_name'][:len(self.data['field_name']) - len(self.Meta.fields[int(self.data['num']) - 1])]
            print(self.data)
            print(self.prefix)
            try:
                for item in child_fields:
                    if self.data[self.prefix+parent]:
                        if 'queryset' in dir(self.fields[item]):
                            for field in self.fields_list[:self.fields_list.index(item)]:
                                self.fields[item].queryset = self.fields[item].queryset.filter(**{field: self.data[self.prefix+field]})
                        parent = item
            except ValueError:
                breakpoint()


    #  ФОРМА СТАЛА СОХРАНЯТЬСЯ ВМЕСТЕ В ДОПОЛНИТЕЛЬНЫМИ ПЕРЕМЕННЫМИ JS