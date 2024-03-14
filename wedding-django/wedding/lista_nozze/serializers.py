from rest_framework import serializers
from .models import Item, Friend, Food

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'title', 'price', 'picture', 'quantity', 'category']


class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friend
        fields = ['id', 'name', 'email', 'comment', 'item_titles', 'item_price']

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ['id', 'name', 'comment']