from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet, FriendViewSet, FoodViewSet

router = DefaultRouter()
router.register(r'items', ItemViewSet)
router.register(r'friends', FriendViewSet)
router.register(r'foods', FoodViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
