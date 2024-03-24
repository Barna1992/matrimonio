from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet, FriendViewSet, FoodViewSet
from .views import SurveyCreateView, SurveyListView



router = DefaultRouter()
router.register(r'items', ItemViewSet)
router.register(r'friends', FriendViewSet)
router.register(r'foods', FoodViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('survey/create/', SurveyCreateView.as_view(), name='survey-create'),
    path('survey/list/', SurveyListView.as_view(), name='survey-list'),
]
