from django.conf.urls import url, include

from rest_framework import routers

from academic import rest_views

router = routers.DefaultRouter()
router.register(
    r'Todo',
    rest_views.TodoViewSet,
    base_name='todo'
)
router.register(
    r'Schedule',
    rest_views.ScheduleViewSet,
    base_name='schedule'
)

urlpatterns = router.urls
