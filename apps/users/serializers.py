import re
from rest_framework import serializers
from django.contrib.auth import get_user_model
from datetime import datetime
from datetime import timedelta
from rest_framework.validators import UniqueValidator
from rest_framework.validators import UniqueValidator

User = get_user_model()


class UserRegSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True, allow_blank=False,
                                     validators=[UniqueValidator(queryset=User.objects.all(), message="user already exists")])
    password = serializers.CharField(
        style={'input_type':'password'}, write_only=True,
    )

    # def create(self, validated_data):
    #     user = super(UserRegSerializer, self).create(validated_data=validated_data)
    #     user.set_password(validated_data["password"])
    #     user.save()
    #     return user

    class Meta:
        model = User
        fields = ("username","password")

class UserDetailSerializer(serializers.ModelSerializer):
    '''
    User detail serializer
    '''
    class Meta:
        model = User
        fields = ("name", "gender", "birthday", "email", "mobile")
