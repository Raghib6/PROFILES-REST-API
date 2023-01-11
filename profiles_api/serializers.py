from rest_framework import serializers
from .models import UserProfile, ProfileFeedItem


class HelloSerializer(serializers.Serializer):
    """Serializers a name field for testing our APIView"""

    name = serializers.CharField(max_length=10)


class UserProfileSerilalizer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ["id", "email", "name", "password"]
        extra_kwargs = {
            "password": {"write_only": True, "style": {"input_type": "password"}}
        }

    # If we don't override the create function it will use default create method insted of create_user method and
    # save password as clear text instead of hashed password.
    def create(self, validated_data):
        """Create and return a new user"""
        user = UserProfile.objects.create_user(  # create_user is a function from UserProfileManager
            email=validated_data["email"],
            name=validated_data["name"],
            password=validated_data["password"],
        )
        return user


class ProfileFeedItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileFeedItem
        fields = ["id", "user_profile", "status_text", "created_on"]
        extra_kwargs = {"user_profile": {"read_only": True}}
