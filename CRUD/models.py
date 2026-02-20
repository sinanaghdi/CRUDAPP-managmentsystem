from django.db import models

# Create your models here.


class employee(models.Model):
    fullname = models.CharField(max_length=100 , unique=True)
    salary = models.PositiveIntegerField(max_length=60000000)
    hired_date = models.DateField(blank=True, unique=True)     

    def __str__(self):
        return super().__str__()
    
