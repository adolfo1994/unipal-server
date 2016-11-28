from django.conf.urls import include, url

from rest_framework import routers

from accounts import rest_views

router = routers.DefaultRouter()
router.register(
    r'Users',
    rest_views.UserViewSet,
    base_name='users'
)
router.register(
    r'Follow',
    rest_views.FollowViewSet,
    base_name='follow'
)


urlpatterns = [
    url(r'^', include(router.urls))
]
