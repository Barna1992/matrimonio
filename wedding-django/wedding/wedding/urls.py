"""
URL configuration for wedding project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from lista_nozze.views import index, lista, cart, summary, thanks, food

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('lista_nozze.urls')),
    path('', index, name='index'),
    path('food', food, name='food'),
    path('lista_nozze/', lista, name='lista'),
    path('lista_nozze/cart/', cart, name='lista'),
    path('lista_nozze/summary/', summary, name='lista'),
    path('lista_nozze/thanks/', thanks, name='lista'),
]
