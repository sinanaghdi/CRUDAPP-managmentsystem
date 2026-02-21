from django.db import models

class employee(models.Model):
    fullname = models.CharField(max_length=100)
    role = models.CharField(max_length=50, default=None)
    salary = models.PositiveIntegerField()  # ✅ حذف max_length
    hired_date = models.DateField(blank=True)  # ✅ حذف unique=True
    Email = models.CharField(max_length=60, unique=True, default=None)   

    def __str__(self):
        return f"{self.fullname}"