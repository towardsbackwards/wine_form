from django.contrib import admin
from mainapp.models import CountryModel, RegionModel, AreaModel, MarkModel, SignModel, MetaModel
admin.site.register(MetaModel)
admin.site.register(CountryModel)
admin.site.register(RegionModel)
admin.site.register(AreaModel)
admin.site.register(MarkModel)
admin.site.register(SignModel)
