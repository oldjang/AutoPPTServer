from django.contrib import admin

# Register your models here.
from api.models import Template


@admin.register(Template)
class TemplateAdmin(admin.ModelAdmin):
    list_display = ('pk', 'image_url', 'template_url')