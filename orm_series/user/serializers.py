from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.core.validators import MinLengthValidator

User = get_user_model()


class UserRegistrationSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField(required=True)
    password = serializers.CharField(
        write_only=True, 
        required=True, 
        style={'input_type': 'password'}, 
        validators=[MinLengthValidator(8)]  
    )
    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email is already in use.")
        return value
        

    # def create(self, validated_data):
    #     user = User.objects.create_user(email=validated_data['email'], password=validated_data['password'])
    #     user.first_name = validated_data.get('first_name', '')  # Optional: Set first_name if provided
    #     user.last_name = validated_data.get('last_name', '')  # Optional: Set last_name if provided
    #     user.save()
    #     return user