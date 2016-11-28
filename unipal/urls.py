"""unipal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from push_notifications.api.rest_framework import GCMDeviceAuthorizedViewSet

from django.conf.urls import include, url
from django.contrib import admin

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'device/gcm', GCMDeviceAuthorizedViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^jet/', include('jet.urls', 'jet')),
    url(r'^friendship/', include('friendship.urls')),
    url(r'api/academic/', include('academic.urls')),
    url(r'api/accounts/', include('accounts.urls'))
]
