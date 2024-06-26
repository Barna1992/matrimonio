from django.db import models

CATEGORY_CHOICES = [
    ('travel', 'travel'),
    ('home', 'home'),
]

class Item(models.Model):
    title = models.CharField(max_length=200)
    price = models.IntegerField()
    picture = models.ImageField(upload_to='pictures/', blank=True, null=True)
    quantity = models.IntegerField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='travel')
    ordering = models.IntegerField(default=0) 

    def __str__(self):
        return self.title


class Friend(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=50)
    comment = models.TextField()
    item_titles = models.CharField(max_length=255)  
    item_price = models.FloatField() 

    def __str__(self):
        return self.name
    
class Food(models.Model):
    name = models.CharField(max_length=255)
    allergie = models.TextField()
    pesce = models.BooleanField(default=True)
    vegetariano = models.BooleanField(default=False)


    def __str__(self):
        return self.name
    

class Survey(models.Model):
    nome = models.CharField(max_length=100)
    salgo_al_rifugio = models.BooleanField()
    dormo_al_rifugio = models.BooleanField()
    numero_di_persone = models.PositiveIntegerField()

    def __str__(self):
        return self.nome
