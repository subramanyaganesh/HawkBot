# app_name/urls.py
from django.urls import path
from .views import get_json_response

urlpatterns = [
    path('getAnswer/',get_json_response,name='finalResponse'),
]
