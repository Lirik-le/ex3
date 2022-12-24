from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'item', ItemAPIView)
router.register(r'user', UserAPIView)


urlpatterns = [
    path('', include(router.urls)),
    path('login', include('rest_framework.urls')),
]
