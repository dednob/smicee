from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


class UserSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = User
        fields = ['email', 'username', 'last_name', 'first_name', 'password']
       

    def save(self):
        user = User(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
            last_name=self.validated_data['last_name'],
            first_name=self.validated_data['first_name'],
        )
        # if User.objects.filter(email=user.email).exists():
        #     raise serializers.ValidationError("Email exists")
        password = self.validated_data['password']
        user.set_password(password)
        user.save()

        return user

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields =('__all__')