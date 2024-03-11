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