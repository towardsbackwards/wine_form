from django.contrib import admin
from mainapp.models import CountryModel, RegionModel, AreaModel, MarkModel, SignModel

admin.site.register(CountryModel)
admin.site.register(RegionModel)
admin.site.register(AreaModel)
admin.site.register(MarkModel)
admin.site.register(SignModel)