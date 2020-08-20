from django.urls import path
from .views import *

app_name = 'community'

urlpatterns = [
    path('qna/', qna, name='qna'),
    path('notice/', notice, name='all_notice'),
    path('qna/', event, name='all_event'),
]
