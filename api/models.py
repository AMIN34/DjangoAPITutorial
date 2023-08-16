from django.db import models

# Create your models here.
class PowerData(models.Model):
    voltage = models.CharField(max_length=10)
    current = models.CharField(max_length=10)
    power = models.CharField(max_length=10)
    energy = models.CharField(max_length=10)
    
    
    def __str__(self):
        return f'PowerData(id={self.id})'
    

class File(models.Model):
    file = models.FileField(upload_to='uploads/')
    upload_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.file.name