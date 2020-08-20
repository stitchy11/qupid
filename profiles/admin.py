from django.contrib import admin

from .models import *

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug':('name',)}


class CharacterAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Character._meta.get_fields() if f.name != 'profile']

admin.site.register(Character, CharacterAdmin)
admin.site.register(Profile, ProfileAdmin)
# Register your models here.
