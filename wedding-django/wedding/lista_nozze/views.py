from rest_framework import viewsets
from .models import Item, Friend, Food
from .serializers import ItemSerializer, FriendSerializer, FoodSerializer
from rest_framework.response import Response
from rest_framework import status

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class FriendViewSet(viewsets.ModelViewSet):
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer

    def create(self, request, *args, **kwargs):
        items = request.data.pop('string_ids', [])
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            for item in items:
                item_id, item_quantity = item.split('-')
                current = Item.objects.get(id=item_id)
                current.quantity -= int(item_quantity)
                current.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

from django.shortcuts import render

def item_list(request):
    items = Item.objects.all()
    return render(request, 'lista_nozze/item_list.html', {'items': items})

def index(request):
    return render(request, 'lista_nozze/index.html')

def lista(request):
    return render(request, 'lista_nozze/lista_nozze.html')

def cart(request):
    return render(request, 'lista_nozze/cart-page.html')

def summary(request):
    return render(request, 'lista_nozze/summary-page.html')

def thanks(request):
    return render(request, 'lista_nozze/thanks.html')

def food(request):
    return render(request, 'food.html')