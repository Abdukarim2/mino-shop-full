import uuid
import json
from django.db import models
from minoapp.models import Product

# Create your models here.
class Order(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    location = models.CharField(max_length=150)
    phone_number = models.IntegerField()
    index = models.IntegerField(blank=True, null=True)
    pay_type = models.CharField(max_length=20)
    coupon = models.CharField(max_length=20, blank=True)
    products = models.JSONField()
    confirm = models.BooleanField(blank=True, default=False)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    delivered = models.BooleanField(blank=True, default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.surname}"

    class Meta:
        ordering = ['-id']
        