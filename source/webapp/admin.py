from django.contrib import admin
from webapp.models import HostBook


class HostBookAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'email', 'status']
    list_filter = ['name', 'status']
    list_display_links = ['pk', 'name']
    search_fields = ['name', 'text']
    fields = ['name', 'email', 'text', 'status', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']


admin.site.register(HostBook, HostBookAdmin)