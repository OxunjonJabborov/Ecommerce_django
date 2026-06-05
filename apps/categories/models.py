from django.db import models

from apps.common.models import BaseModel

# Create your models here.

class Category(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    icon = models.ImageField(upload_to='categories/', null=True, blank=True)

    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='subcategories')

    def __str__(self):
        return self.name