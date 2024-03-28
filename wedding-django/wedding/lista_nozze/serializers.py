from rest_framework import serializers
from .models import Item, Friend, Food, Survey

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        ordering = ['ordering']
        fields = '__all__'


class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friend
        fields = ['id', 'name', 'email', 'comment', 'item_titles', 'item_price']

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ['id', 'name', 'comment']

class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = '__all__'