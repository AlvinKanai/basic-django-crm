from django.shortcuts import render
from django.views import generic

# Create your views here.
class LandingPageView(generic.TemplateView):
    template_name = "landing_page.html"
