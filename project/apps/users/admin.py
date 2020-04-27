from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import EdenUser

admin.site.register(EdenUser, UserAdmin)
