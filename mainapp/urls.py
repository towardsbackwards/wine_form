import os
from django.urls import path, include
from mainapp.views import CountryCreateView, ViewJS

app_name = os.path.basename(os.path.dirname(os.path.abspath(__file__)))

urlpatterns = [
    path('', CountryCreateView.as_view(), name='Index'),
    path('country-form-data/', ViewJS.as_view(), name='FormJS')
]
