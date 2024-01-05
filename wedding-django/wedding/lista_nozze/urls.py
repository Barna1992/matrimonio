from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet, FriendViewSet

router = DefaultRouter()
router.register(r'items', ItemViewSet)
router.register(r'friends', FriendViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
