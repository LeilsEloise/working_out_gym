from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Comment, Post


# Register your models here.
@admin.register(Post)
# Project 3 PostAdmin class code for SumemrnoteModel
class PostAdmin(SummernoteModelAdmin):
    list_display = ("title", "slug", "created_on")
    search_fields = ["title", "content"]
    list_filter = ("title", "slug", "created_on")
    prepopulated_fields = {"slug": ("title",)}
    summernote_fields = ("content",)


admin.site.register(Comment)
