from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name=models.CharField( max_length=100)
    website=models.URLField( default='')
    date_opened=models.DateField( auto_now=False, auto_now_add=False)
    latitude=models.FloatField()
    longtitude=models.FloatField()

    """"returning the name of the model field"""
    def __str__(self):
        return self.name
    