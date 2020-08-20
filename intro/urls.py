from django.urls import path
from .views import *

app_name = 'intro'

urlpatterns = [
    path('', intro, name='intro'),

]
