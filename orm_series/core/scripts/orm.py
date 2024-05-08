from core.models import *
from user.models import *
from django.utils import timezone
from django.db import connection
from django.contrib.auth import get_user_model
User=get_user_model()
def run():
    User.objects.create(email="admin3304@gamil.com",password="admin123")
    # restaurant=Restaurant.objects.first()
    # user=User.objects.first()
    # Rating.objects.create(user=user,restaurant=restaurant,rating=5)
    # Restaurant.objects.create(
    #     name="Pizza Shop",
    #     website="www.mypizzashop.com",
    #     date_opened=timezone.now(),
    #     latitude=200.4,
    #     longtitude=200.4,
    #     restuarant_type="IT",
    # )
    # print(connection.queries)