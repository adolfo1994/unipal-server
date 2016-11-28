from django.contrib.auth.models import User
from friendship.models import Follow
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email')


class UserFollowerSerializer(serializers.ModelSerializer):

    follower = UserSerializer()
    followee = UserSerializer()

    class Meta:
        model = Follow
        fields = ('follower', 'followee')


class FollowSerializer(serializers.ModelSerializer):

    class Meta:
        model = Follow
        fields = ('follower', 'followee')


class UserFollowSerializer(serializers.ModelSerializer):

    following = serializers.SerializerMethodField()

    def get_following(self, obj):
        query = Follow.objects.filter(follower=obj)
        return UserFollowerSerializer(query, many=True).data

    class Meta:
        model = User
        fields = ('following', )
