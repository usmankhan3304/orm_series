from django.shortcuts import render,HttpResponse
from django.contrib.auth import get_user_model
from rest_framework import viewsets, status
# Create your views here.
# views.py
User=get_user_model()
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserRegistrationSerializer
User=get_user_model()

class UserRegistrationAPIView(viewsets.ViewSet):
    
    def get_serializer_class(self):
        return UserRegistrationSerializer
    
    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()  # Get the serializer class
        return serializer_class(*args, **kwargs)  # Instantiate the serializer with arguments
    
    def create(self, request):
        data = request.data
        serializer = UserRegistrationSerializer(data=data)
        if serializer.is_valid():
            first_name = data.get('first_name')
            last_name = data.get('last_name')
            email = data.get('email')
            password = data.get('password')
            # Create the user object
            user = User.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email
            )
            user.set_password(password)
            user.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request):
        users = User.objects.all()  # Retrieve all users from the database
        serializer = self.get_serializer(users, many=True)  # Serialize the queryset
        return Response(serializer.data, status=status.HTTP_200_OK)
    # def get(self, request):
    #     users = User.objects.all()  # Retrieve all user objects from the database
    #     serializer = UserRegistrationSerializer(users, many=True)  # Serialize all users
    #     return Response(serializer.data)  # Return serialized user data

    # def post(self, request):
    #     serializer = UserRegistrationSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)