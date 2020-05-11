from django.forms import ModelForm

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
            if 'field_name' in self.data and 'num' in self.data:
                #  для избежания ошибки MultiValueDictKeyError (из-за переменных 'num' и 'active_field')
                active_field = self.data['field_name']
                num = self.data['num']
                self.data._mutable = True
                self.data.pop('field_name')
                self.data.pop('num')
            else:
                active_field = self.fields_list[-1]
                num = len(self.fields)

            self.prefix = active_field[:len(active_field) - len(self.Meta.fields[int(num) - 1])]

            for item in child_fields:
                if self.data[self.prefix+parent]:
                    if 'queryset' in dir(self.fields[item]):
                        for field in self.fields_list[:self.fields_list.index(item)]:
                            self.fields[item].queryset = self.fields[item].queryset.filter(**{field: self.data[self.prefix+field]})
                        if len(self.fields[item].queryset) == 0:  # len, а не count() чтобы не обращаться к БД каждый раз
                            for child in self.fields_list[self.fields_list.index(item):]:
                                self.fields[child].widget.attrs['style'] = 'visibility: hidden'  # скрывает все поля ниже item
                    parent = item
                else:
                    self.fields[item].widget.attrs['style'] = 'visibility: hidden'
        else:
            for item in child_fields:
                self.fields[item].widget.attrs['style'] = 'visibility: hidden'
