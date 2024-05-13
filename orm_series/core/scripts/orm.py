from core.models import *
from user.models import *
from django.utils import timezone
from django.db import connection
from django.contrib.auth import get_user_model
User=get_user_model()
def run():
    # Sale.objects.create(restaurant=Restaurant.objects.get(pk=1),
    #                     income=234444.3,
    #                     date_time=timezone.now())
    # User.objects.create(email="admin3304@gamil.com",password="admin123")
    # restaurant=Restaurant.objects.get(pk=2)
    # user=User.objects.get(pk=8)
    # # for user in users:
    # #     print(user.id)
    
    # Rating.objects.create(user=user,restaurant=restaurant,rating=3)

   
    # Restaurant.objects.create(
    #     name="Pizza Shop",
    #     website="www.mypizzashop.com",
    #     date_opened=timezone.now(),
    #     latitude=200.4,
    #     longtitude=200.4,
    #     restuarant_type="IT",
    # )
    # print(connection.queries)

    # filters=Rating.objects.get(pk=1)
    # print(filters.restaurant)
    # print(connection.queries)

    # get_or_create method in django...
    obj, created = Rating.objects.get_or_create(
    restaurant=Restaurant.objects.get(pk=1),
    user=User.objects.get(pk=1),
    rating=1)
    
    if created:
        print('Object created:', obj)
       
    else:
        print('Object retrieved:', obj)
        print(obj.restaurant)