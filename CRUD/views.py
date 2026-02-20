from django.shortcuts import render
from django.views.generic import ListView , CreateView , DeleteView, UpdateView , DetailView
from django.urls import reverse_lazy
# Create your views here.
from .models import employee
from .form import EmployeeForm

class EmployeeListView(ListView):
    model = employee
    template_name = 'templates/CRUD/employee_list.html'
    context_object_name = 'Employees'
    
# class EmployeeDetailView(DetailView):
#     model = employee
#     template_name = 'templates/employees/employee_detail.html'


# class EmployeeDeleteView(DeleteView):
#     model = employee
#     template_name = 'templates/employees/employee_confirm_delete.html'
#     success_url = reverse_lazy('employee_list')

# class 
