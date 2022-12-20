from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=7, decimal_places=0)
    digital = models.BooleanField(default=False, null=True, blank=True)
    image = models.CharField(max_length=1087)
    
    class Meta:
          verbose_name_plural = "store"
    
    def __str__(self):
        return self.name





    





