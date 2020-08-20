from django.urls import path
from .views import *

app_name = 'profiles'

urlpatterns = [
    path('', all_profiles, name='all_profiles'),
    # path('detail/<int:id>', detail_profile, name="detail_profile")
    # path('<int:id>/<profile_slug>/', all_profiles, name='all_profiles')
    # path('<int:id>/', )
]
