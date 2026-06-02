from django.db import models

from apps.products.models import Product
from apps.common.models import BaseModel

# Create your models here.

class Category(BaseModel):
    name = models.CharField(max_length=255)
    products = models.ManyToManyField(Product, related_name='categories')

    def __str__(self):
        return self.name
