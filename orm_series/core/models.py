from django.db import models
from django.contrib.auth import get_user_model

from django.utils.translation import gettext as _
User=get_user_model()
# Create your models here.
class Restaurant(models.Model):
    Type_choices=STATUS_CHOICES = [
        ('IN', 'India'),
        ('CH', 'Chinese'),
        ('IT', 'Italain'),
        ('MX', 'Mexican'),
        ('GR', 'Greek'),
        ('OT', 'Other'),
    ]
    
    name=models.CharField( max_length=100)
    website=models.URLField(default='')
    date_opened=models.DateField( auto_now=False, auto_now_add=False)
    latitude=models.FloatField()
    longtitude=models.FloatField()
    restuarant_type=models.CharField( max_length=2,choices=Type_choices)

    """"returning the name of the model field"""
    def __str__(self):
        return self.name
    
class Rating(models.Model):
    user=models.ForeignKey(User,  on_delete=models.CASCADE)
    restaurant=models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    rating=models.PositiveIntegerField()

    def __str__(self):
        return f"Rating {self.rating}"
    
class Sale(models.Model):
    restaurant=models.ForeignKey(Restaurant,  on_delete=models.SET_NULL, null=True)
    income=models.DecimalField( max_digits=8, decimal_places=2)
    date_time=models.DateTimeField()

class MyModel(models.Model):
    STATE_CHOICES = [
        (0, 'Approved'),
        (1, 'Rejected')
    ]
    
    state = models.IntegerField(choices=STATE_CHOICES)