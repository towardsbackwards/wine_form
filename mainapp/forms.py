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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        parent, child_fields = self.fields_list[0], self.fields_list[1:]
        attrs_dict = {'onchange': 'addForm(this)', 'class': 'form-control', 'data-url': self.data_url}
        for field_name, field in self.fields.items():
            self.fields[field_name].widget.attrs.update(attrs_dict)
        if self.data:
            breakpoint()
            for item in child_fields:
                if self.data[parent]:  # если есть данные в первом поле
                    if 'queryset' in dir(self.fields[item]):
                        for field in self.fields_list[:self.fields_list.index(item)]:
                            self.fields[item].queryset = self.fields[item].queryset.filter(**{field: self.data[field]})
                        if len(self.fields[item].queryset) == 0:
                            for child in self.fields_list[self.fields_list.index(item):]:
                                self.fields[child].widget.attrs['style'] = 'visibility: hidden'
                    parent = item
                else:
                    self.fields[item].widget.attrs['style'] = 'visibility: hidden'
        else:
            for item in child_fields:
                self.fields[item].widget.attrs['style'] = 'visibility: hidden'
