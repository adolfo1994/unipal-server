from django.contrib.auth.models import User
from friendship.models import Follow
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email')


class FollowSerializer(serializers.ModelSerializer):

    class Meta:
        model = Follow
        fields = ('follower', 'followee')
