from django.shortcuts import redirect, reverse
from django.views import generic
from django.core.mail import send_mail
from .models import Lead
from .forms import LeadModelForm

# Create your views here.


class LeadListView(generic.ListView):
    template_name = "leads/lead_list.html"
    queryset = Lead.objects.all()
    context_object_name = 'leads'


class LeadDetailView(generic.DetailView):
    template_name = 'leads/lead_detail.html'
    queryset = Lead.objects.all()
    context_object_name = 'lead'


class LeadCreateView(generic.CreateView):
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


class LeadUpdateView(generic.UpdateView):
    template_name = 'leads/lead_update.html'
    queryset = Lead.objects.all()
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse('leads:lead-list')


class LeadDeleteView(generic.DeleteView):
    template_name = 'leads/lead_delete.html'
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse('leads:lead-list')
