from django.shortcuts import reverse
from django.views import generic
from .forms import CustomUserCreationForm

# Create your views here.


class LandingPageView(generic.TemplateView):
    template_name = "pages/landing_page.html"


class SignUpView(generic.CreateView):
    template_name = 'registration/signup.html'
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse('login')
