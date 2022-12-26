from django.shortcuts import render
from django.views.generic import TemplateView

class HomeMain(TemplateView):
    template_name = 'MainHome.html'
