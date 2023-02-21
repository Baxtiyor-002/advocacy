from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Initiative


# Create your views here.

class HomePageView(ListView):
    model = Initiative
    template_name = 'home.html'


class InitiativeDetailView(DetailView):
    model = Initiative
    template_name = 'initiative_detail.html'