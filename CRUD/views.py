from django.shortcuts import render
from django.views.generic import ListView , CreateView , DeleteView, UpdateView , DetailView
from django.urls import reverse_lazy
# Create your views here.
from .models import employee
# from .form import EmployeeForm

class EmployeeListView(ListView):
    model = employee
    template_name = 'CRUD/employee_list.html'
    context_object_name = 'employees'
    
    def get_queryset(self):
        qs = super().get_queryset()
        print("Queryset:", qs)  # این رو در ترمینال ببین
        return qs
    
# class EmployeeDetailView(DetailView):
#     model = employee
#     template_name = 'templates/employees/employee_detail.html'


# class EmployeeDeleteView(DeleteView):
#     model = employee
#     template_name = 'templates/employees/employee_confirm_delete.html'
#     success_url = reverse_lazy('employee_list')

# class 
