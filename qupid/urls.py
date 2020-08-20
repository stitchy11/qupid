from django.urls import path
from .views import *

app_name = 'qupid'

urlpatterns = [
    path('', main, name='main'),
]
