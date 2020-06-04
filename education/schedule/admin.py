from django.contrib import admin
from .models import Schedule


# Register your models here.

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = "id", "date", "title", "group"
    list_display_links = "id", "title",
