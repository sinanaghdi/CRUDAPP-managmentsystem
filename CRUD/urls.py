from django.contrib import admin
from django.urls import path , include
from .views import EmployeeListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', EmployeeListView.as_view(), name= 'employee_list'),
    
]
