from django.contrib import admin

from .models import Feedback


# Register your models here.
@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ("created_on", "email", "user", "handled")
    list_filter = ("handled", "created_on")
    search_fields = ("email", "name", "message")
