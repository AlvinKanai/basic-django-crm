from django.shortcuts import redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.core.mail import send_mail
from .models import Lead
from .forms import LeadModelForm, AssignAgentForm
from agents.mixins import OrganizerAndLoginRequiredMixin

# Create your views here.


class LeadListView(LoginRequiredMixin, generic.ListView):
    template_name = "leads/lead_list.html"
    context_object_name = 'leads'

    def get_queryset(self):
        user = self.request.user
        
        # geting user organization
        if user.is_organizer:
            queryset =  Lead.objects.filter(organization = user.userprofile, agent__isnull = False)
        else:
            queryset =  Lead.objects.filter(organization = user.agent.organization, agent__isnull = False)
            
            queryset = queryset.filter(agent__user = user)
            
        return queryset
    
    
    def get_context_data(self, **kwargs):
        context = super(LeadListView, self).get_context_data(**kwargs)
        user = self.request.user
        if user.is_organizer:
            queryset = Lead.objects.filter(organization = user.userprofile, agent__isnull = True)
        context.update({
            'unassigned_leads': queryset
        })
        return context
    


class LeadDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = 'leads/lead_detail.html'
    context_object_name = 'lead'

    def get_queryset(self):
        user = self.request.user
        
        if user.is_organizer:
            queryset = Lead.objects.filter(organization = user.userprofile)
        else:
            queryset = Lead.onjects.filter(organization = user.agent.organization)
            
            queryset = Lead.objects.filter(agent__user = user)
        
        return queryset


class LeadCreateView(OrganizerAndLoginRequiredMixin, generic.CreateView):
    template_name = 'leads/lead_create.html'
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse('leads:lead-list')

    def form_valid(self, form):
        lead = form.save(commit = False)
        lead.organisation = self.request.user.userprofile
        lead.save()
        # sending emails before it creates the lead
        send_mail(
            subject="You're a lead on Cimply",
            message="You have been added as a new lead on Cimply CRM. Visit cimply.com to view",
            from_email="admin@cimply.com",
            recipient_list=["userone@test.com"],
        )
        return super(LeadCreateView, self).form_valid(form)


class LeadUpdateView(OrganizerAndLoginRequiredMixin, generic.UpdateView):
    template_name = 'leads/lead_update.html'
    form_class = LeadModelForm

    def get_queryset(self):
        user = self.request.user
        queryset = Lead.objects.filter(organization = user.userprofile)
        
        return queryset

    def get_success_url(self):
        return reverse('leads:lead-list')


class LeadDeleteView(OrganizerAndLoginRequiredMixin, generic.DeleteView):
    template_name = 'leads/lead_delete.html'

    def get_queryset(self):
        user = self.request.user
        queryset = Lead.objects.filter(organization = user.userprofile)
        
        return queryset

    def get_success_url(self):
        return reverse('leads:lead-list')
    
class AssignAgentView(OrganizerAndLoginRequiredMixin, generic.FormView):
    template_name = 'leads/assign_agent.html'
    form_class = AssignAgentForm
    
    def get_form_kwargs(self, **kwargs):
        kwargs = super(AssignAgentView, self).get_form_kwargs(**kwargs)
        kwargs.update ({
            'request': self.request
        })
        
        return kwargs
        
    def form_valid(self, form):
        agent = form.cleaned_data['agent']
        lead = Lead.objects.get(id = self.kwargs['pk'])
        lead.agent = agent
        lead.save()
        return super(AssignAgentView, self).form_valid(form)
    
    def get_success_url(self):
        return reverse('leads:lead-list')
