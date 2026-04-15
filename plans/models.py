from django.db import models
from django.contrib.auth.models import User

class Plan(models.Model):
    """ Defines the Nutrition and Fitness Plan model - ChatGPT Code """
    PLAN_TYPE_CHOICES = [
        ('fitness', 'Fitness'),
        ('nutrition', 'Nutrition'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='plans/')
    price = models.DecimalField(max_digits=6, decimal_places=2)

    plan_type = models.CharField(max_length=10, choices=PLAN_TYPE_CHOICES)

    def __str__(self):
        return self.title

class UserPlan(models.Model):
    """ ChatGPT - Enforces the rule that users may only have 1 x purchased fitness and/or nutrition plan at any one time"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} - {self.plan}"