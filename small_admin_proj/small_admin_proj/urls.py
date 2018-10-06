"""small_admin_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from small_admin_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('computer_list/', views.ComputerListView.as_view(), name='computers'),
    path('', views.MapView.as_view(), name='basic'),
    path('employee_list/', views.EmployeeListView.as_view(), name='employee'),
    path('employee_list_all/', views.AllEmployeeListView.as_view(), name='employee-all'),
    path('divisions/', views.DivisionView.as_view(), name='division'),
    path('divisions_detail/<int:division_id>', views.DivisionDetailView.as_view(), name='division-detail'),
    path('employee_list/<int:employee_id>', views.EmployeeDetailView.as_view(), name='employee-detail'),
    path('computer_form/', views.ComputerFormView.as_view(), name='computer_form'),
    path('employee_form/', views.EmployeeFormView.as_view(), name='employee_form'),
    path('edit_employee/<int:employee_id>/', views.EmployeeUpdateView.as_view(), name='employee-edit'),
    path('contact/', views.ContactView.as_view(), name= 'contact'),

]
