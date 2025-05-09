from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["id", "email", "username", "first_name", "last_name", "password", "photo_URL"]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        email = validated_data['email']
        username = validated_data['username']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        password = validated_data['password']
        photo_URL = validated_data['photo_URL']

        user = get_user_model()
        new_user = user.objects.create(email=email, username=username, first_name=first_name, last_name=last_name,
                                       photo_URL=photo_URL)
        new_user.set_password(password)
        new_user.save()
        return new_user


class UpdateUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            "id", "email", "username", "first_name",
            "last_name", "photo_URL"
        ]
