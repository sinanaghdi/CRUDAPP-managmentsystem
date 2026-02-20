from django import forms
from .models import employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = employee
        fields = '__all__'  # همه فیلدها رو شامل کن