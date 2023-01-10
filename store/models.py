from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=10087)
    
    class Meta:
          verbose_name_plural = "store"
    
    def __str__(self):
        return self.name





    





