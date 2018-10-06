from django.shortcuts import render
from django.template.response import TemplateResponse
from django.urls import reverse_lazy
from django.views import generic, View
from django.forms import forms

from small_admin_app.forms import EmployeeCreateForm, ComputerCreateForm
from small_admin_app.models import Computers, ArcMap, Employee, Divisions


class HomeView(generic.TemplateView):
    model = Computers
    template_name = 'base.html'

class ContactView(generic.TemplateView):
    template_name = 'contact.html'

class ComputerListView(generic.ListView):
    model = Computers
    template_name = 'computer_list.html'

class EmployeeListView(generic.ListView):
    model = Employee
    template_name = 'employee_list.html'

class AllEmployeeListView(generic.ListView):
    model = Employee
    template_name = 'employee_list_all.html'

class EmployeeDetailView(View):

    def get(self, request, employee_id):
        employee = Employee.objects.get(pk=employee_id)
        return render(request, 'employee_detail.html', {'employee':employee})

class MapView(generic.TemplateView):
    template_name = 'map_image.html'

class DivisionView(generic.ListView):
    model = Divisions
    template_name = 'divisions_list.html'

class DivisionDetailView(View):

    def get(self, request, division_id):
        divisions = Divisions.objects.get(pk=division_id)
        employee = Employee.objects.filter(division_user=division_id)
        return render(request, 'division_detail.html', {'divisions':divisions,
                                                         'employee': employee})

class ComputerFormView(generic.CreateView):
    form_class = ComputerCreateForm
    template_name = 'computer_form.html'
    success_url = reverse_lazy('computers')

class EmployeeFormView(generic.CreateView):
    form_class = EmployeeCreateForm
    template_name = 'employee_form.html'
    success_url = reverse_lazy('employee-all')


class EmployeeUpdateView(generic.UpdateView):
    model = Employee
    fields =  ['name', 'last_name', 'division_user']
    success_url = reverse_lazy('employee')
    pk_url_kwarg = 'employee_id'

