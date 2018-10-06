from django import forms
from small_admin_app.models import Employee, Computers

class ComputerCreateForm(forms.ModelForm):
    class Meta:
        model = Computers
        fields = ['id_numb', 'name']

class EmployeeCreateForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'last_name', 'division_user', 'user_computer']

