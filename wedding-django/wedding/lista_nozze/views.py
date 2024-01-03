from rest_framework import viewsets
from .models import Item
from .serializers import ItemSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

from django.shortcuts import render

def item_list(request):
    items = Item.objects.all()
    return render(request, 'lista_nozze/item_list.html', {'items': items})
