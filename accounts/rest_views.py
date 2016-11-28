from django.contrib.auth.models import User
from friendship.models import Follow
from rest_framework import viewsets

from accounts.serializers import (
    UserSerializer,
    FollowSerializer,
    UserFollowSerializer
)


class UserViewSet(viewsets.GenericViewSet, viewsets.mixins.ListModelMixin):

    serializer_class = UserSerializer
    queryset = User.objects.all()


class FollowViewSet(viewsets.GenericViewSet, viewsets.mixins.CreateModelMixin):

    serializer_class = FollowSerializer
    queryset = Follow.objects.all()


class UserFollowViewSet(viewsets.GenericViewSet,
                        viewsets.mixins.RetrieveModelMixin):

    serializer_class = UserFollowSerializer
    queryset = User.objects.all()
