from rest_framework import viewsets
from .models import Item, Friend
from .serializers import ItemSerializer, FriendSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class FriendViewSet(viewsets.ModelViewSet):
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer

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