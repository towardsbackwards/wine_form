import os
from django.urls import path
from mainapp.views import SignCreateView, ViewJS, SignFormset

app_name = os.path.basename(os.path.dirname(os.path.abspath(__file__)))

urlpatterns = [
    path('', SignCreateView.as_view(), name='Index'),
    path('formset/', SignFormset.as_view(), name='Sign Formset'),
    path('sign-form-data/', ViewJS.as_view(), name='FormJS')
]
