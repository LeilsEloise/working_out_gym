# ChatGPT Code

from django.db import models
from django.contrib.auth.models import User

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=80, blank=True)
    email = models.EmailField(blank=True)
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    handled = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"Feedback #{self.pk} ({self.email or self.name or 'anonymous'})"