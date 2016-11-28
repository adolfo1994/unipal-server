from django.shortcuts import render

# Create your views here.
from push_notifications.api.rest_framework import GCMDeviceAuthorizedViewSet
from rest_framework import permissions


class GCMDeviceViewSet(GCMDeviceAuthorizedViewSet):

    permission_classes = (permissions.AllowAny, )

    def get_queryset(self):
        return self.queryset.first()
