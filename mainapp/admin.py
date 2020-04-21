from django.contrib import admin
from mainapp.models import Country, Region, Area, QualityMark, Sign

admin.site.register(Country)
admin.site.register(Region)
admin.site.register(Area)
admin.site.register(QualityMark)
admin.site.register(Sign)