from django.contrib import admin

from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = 'pk', 'is_customer', 'contact_info', 'experience'
    list_display_links = 'pk', 'contact_info'