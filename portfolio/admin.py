from django.contrib import admin
from .models import Section
# Register your models here.


class SectionAdmin(admin.ModelAdmin):
    list_display = ("title",)
    prepopulated_fields = {"title_slug": ("title",)}

admin.site.register(Section, SectionAdmin)
