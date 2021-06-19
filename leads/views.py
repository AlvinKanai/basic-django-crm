from django.shortcuts import redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.core.mail import send_mail
from .models import Lead
from .forms import LeadModelForm

# Create your views here.


class LeadListView(LoginRequiredMixin, generic.ListView):
    template_name = "leads/lead_list.html"
    context_object_name = 'leads'

    def get_queryset(self):
        return Lead.objects.all()


class LeadDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = 'leads/lead_detail.html'
    context_object_name = 'lead'

    def get_queryset(self):
        return Lead.objects.all()


class LeadCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = 'leads/lead_create.html'
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse('leads:lead-list')

    def form_valid(self, form):
        # sending emails before it creates the lead
        send_mail(
            subject="You're a lead on Cimply",
            message="You have been added as a new lead on Cimply CRM. Visit cimply.com to view",
            from_email="admin@cimply.com",
            recipient_list=["userone@test.com"],
        )
        return super(LeadCreateView, self).form_valid(form)


class LeadUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'leads/lead_update.html'
    form_class = LeadModelForm

    def get_queryset(self):
        return Lead.objects.all()

    def get_success_url(self):
        return reverse('leads:lead-list')


class LeadDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = 'leads/lead_delete.html'

    def get_queryset(self):
        return Lead.objects.all()

    def get_success_url(self):
        return reverse('leads:lead-list')
