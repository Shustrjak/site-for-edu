from django.contrib import admin
from .models import Teacher, Lesson, Course


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = "id", "full_name", "email"
    list_display_links = "id", "full_name"


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = "id", "title", "short_body", "difficult"
    list_display_links = "id", "title"


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = "id", "title", "short_description", "teacher", "date"
    list_display_links = "id", "title"
