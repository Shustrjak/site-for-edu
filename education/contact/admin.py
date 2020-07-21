from django.contrib import admin
from .models import Feedback


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = "id", "input_name", "input_mail", "input_text", "copy"
    list_display_links = "id", "input_mail"

    actions = ['update_feedback']

    def update_feedback(self, request, queryset):
        pass
