from django.db import models

# Create your models here.


class employee(models.Model):
    fullname = models.CharField(max_length=100)
    role = models.CharField(max_length=50 ,default=None)
    salary = models.PositiveIntegerField(max_length=60000000)
    hired_date = models.DateField(blank=True, unique=True)  
    Email = models.CharField(max_length=60 , unique=True , default=None)   

    def __str__(self):
        return f"{self.fullname}"
    
    
    
