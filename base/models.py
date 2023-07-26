from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth.models import Meals
# Create your models here.


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    #foodName = models.CharField(max_length=200)
    #category = models.CharField(max_length=50)
    #calory = models.IntegerField()
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['complete']

class Meal(models.Model):
    foodName = models.CharField(max_length=200)
    category = models.CharField(max_length=50)
    calories = models.IntegerField()
    fat = models.FloatField()
    carbohydrate = models.FloatField()
    protein = models.FloatField()
    offeredFood = models.BooleanField(default=False)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.foodName

        