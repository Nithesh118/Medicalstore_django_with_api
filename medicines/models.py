from django.db import models

class Medicine(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField( default=0)
    
    def __str__(self):
        return self.name
    
from django.db import models
from django.core.validators import MinLengthValidator

class Customer(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=10,validators=[MinLengthValidator(8)])
    




