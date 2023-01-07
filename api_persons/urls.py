from rest_framework import routers
from .api import PersontViewSet

router=routers.DefaultRouter()

router.register('api/person',PersontViewSet)
urlpatterns=router.urls


