from django.db import models

# Create your models here.
class PowerData(models.Model):
    voltage = models.CharField(max_length=10)
    current = models.CharField(max_length=10)
    power = models.CharField(max_length=10)
    energy = models.CharField(max_length=10)
    
    
    def __str__(self):
        return f'PowerData(id={self.id})'
    
    