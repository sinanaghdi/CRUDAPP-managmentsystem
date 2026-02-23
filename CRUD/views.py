from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import employee
from .form import EmployeeForm

class EmployeeListView(ListView):
    model = employee
    template_name = 'CRUD/employee_list.html'
    context_object_name = 'employees'

class EmployeeCreateView(CreateView):
    model = employee
    form_class = EmployeeForm
    template_name = 'CRUD/employee_form.html'
    success_url = reverse_lazy('employee_list')

class EmployeeDetailView(DetailView):
    model = employee
    template_name = 'CRUD/employee_detail.html'
    context_object_name = 'employee'

class EmployeeUpdateView(UpdateView):
    model = employee
    form_class = EmployeeForm
    template_name = 'CRUD/employee_form.html'
    success_url = reverse_lazy('employee_list')

class EmployeeDeleteView(DeleteView):
    model = employee
    template_name = 'CRUD/employee_confirm_delete.html'
    success_url = reverse_lazy('employee_list')