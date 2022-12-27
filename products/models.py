from django.db import models
from uuid import uuid4

# Create your models here.

class Provider(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083, default='https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.freepik.es%2Ffotos-vectores-gratis%2Ffondo&psig=AOvVaw3Z0Z0Z0Z0Z0Z0Z0Z0Z0Z0Z&ust=1634040000000000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCJjX2fjX3vMCFQAAAAAdAAAAABAD')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name
