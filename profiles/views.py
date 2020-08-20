from django.shortcuts import render, get_object_or_404
from .models import *


# def all_profiles(request, profile_slug=None):
#     profile = get_object_or_404(Profile, slug=profile_slug)
#     return render(request, 'profiles/all_profiles.html', {'profiles':profile})
#

def all_profiles(request):
    profile = Profile.objects.all()
    return render(request, 'profiles/all_profiles.html', {'profiles':profile})
#
#
# def profile_detail(request, id, profile_slug=None):
#     profile = get_object_or_404(Profile, id=id, slug=profile_slug)
#     return render(request, 'profiles/profile_detail.html', {'profile':profile})


