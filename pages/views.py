from django.shortcuts import render

from django.views.generic import TemplateView

# Create your views here.
class PersonalPageView(TemplateView):
    template_name='personal.html'

class EducationPageView(TemplateView):
    template_name='education.html'