from django.contrib import admin

from .models import Project


class ProjectAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'created_at', 'category']
    list_filter = ['category']


admin.site.register(Project, ProjectAdmin)
