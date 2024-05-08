from django.shortcuts import render,HttpResponse
from django.contrib.auth import get_user_model
# Create your views here.
# views.py
User=get_user_model()
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserRegistrationSerializer,UserSerializer

class UserRegistrationAPIView(APIView):
    def get(self, request):
        users = User.objects.all()  # Retrieve all user objects from the database
        serializer = UserSerializer(users, many=True)  # Serialize all users
        return Response(serializer.data)  # Return serialized user data
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)