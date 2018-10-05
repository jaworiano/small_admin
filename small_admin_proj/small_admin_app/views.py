from django.shortcuts import render
from django.views import generic

from small_admin_app.models import Computers, ArcMap

class HomeView(generic.TemplateView):
    model = Computers
    template_name = 'base.html'
    

class ComputerListView(generic.ListView):
    model = Computers
    template_name = 'computer_list.html'

