from rest_framework import serializers
from profile_api import models


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our apiview"""

    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = models.UserProfile
        fields = ('id','name','email','password')
        extra_kwargs = {
            'password':{
                'write_only':True,
                'style':{'input_type':'password'}
            }
        }

    def create(self,validate_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email = validate_data['email'],
            name = validate_data['name'],
            password = validate_data['password']
        )

        return user

    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)
