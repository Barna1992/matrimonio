from django.db import models

class Item(models.Model):
    title = models.CharField(max_length=200)
    price = models.IntegerField()
    picture = models.ImageField(upload_to='pictures/', blank=True, null=True)
    quantity = models.IntegerField()

    def __str__(self):
        return self.title
