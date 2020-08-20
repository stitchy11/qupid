from django.urls import path
from .views import *

app_name = 'shop'

urlpatterns = [
    path('', product, name='all_product'),
]
