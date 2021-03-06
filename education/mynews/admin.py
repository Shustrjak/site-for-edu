from django.contrib import admin
from .models import Author, Article


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = "id", "first_name", "last_name", "full_name"
    list_display_links = "id", "full_name"


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = "id", \
                   "title", \
                   "short_text", \
                   "author", \
                   "time_to_read", \
                   "ts_created", \
                   "ts_last_changed"
    list_display_links = "id", "title", "short_text"
