from rest_framework import routers

from device import rest_views

router = routers.DefaultRouter()
router.register(
    r'gcm',
    rest_views.GCMDeviceViewSet,
    base_name='gcm'
)

urlpatterns = router.urls
