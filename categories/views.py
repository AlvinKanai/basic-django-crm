from django.shortcuts import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from agents.mixins import OrganizerAndLoginRequiredMixin
from django.views import generic
from .forms import LeadCategoryUpdateForm, CreateCategoryForm
from leads.models import Lead, Category

# Create your views here.
class CategoryListView(LoginRequiredMixin, generic.ListView):
    template_name = 'categories/category_list.html'
    context_object_name = 'categories'
    
    def get_queryset(self):
        user  = self.request.user
        
        if user.is_organizer:
            queryset = Category.objects.filter(organization = user.userprofile)
        else:
            queryset = Category.objects.filter(organization = user.agent.organization)
            
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        user = self.request.user
        
        if user.is_organizer:
            queryset = Lead.objects.filter(organization = user.userprofile)
        else:
            queryset = Lead.objects.filter(organization = user.agent.organization)
        
        context.update({
            'unassigned_lead_count' : Lead.objects.filter(category__isnull = True).count()
        })
        return context
    
class CategoryDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = 'categories/category_detail.html'
    context_object_name = 'category'
    
    def get_queryset(self):
        user = self.user.request
        if user.is_organizer:
            queryset = Category.objects.filter(organization = user.userprofile)
        else:
            queryset = Category.objects.filter(organization = user.agent.organization)
            
        return queryset
    
    # done on category detail template
    # def get_context_data(self, **kwargs):
    #     context = super(CategoryDetailView, self).get_context_data(**kwargs)
    #     user = self.request.user
    #     leads = self.get_object().leads.all()
        
    #     context.update({
    #         'leads': leads
    #     })
        
        # return context    
    
class LeadCategoryUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'categories/lead_category_update.html'
    form_class = LeadCategoryUpdateForm
    
    def get_queryset(self):
        user = self.request.user
        
        if user.is_organizer:
            queryset =  Lead.objects.filter(organization = user.userprofile)
        else:
            queryset = Lead.objects.filter(organization = user.agent.organization)
            
        return queryset
    
    def get_success_url(self):
        return reverse('leads:lead-detail', kwargs={'pk': self.get_object().id})
    
class CategoryCreateView(OrganizerAndLoginRequiredMixin, generic.CreateView):
    template_name = 'categories/category_create.html'
    form_class = CreateCategoryForm
    
    def get_success_url(self):
        return reverse('categories:category-list')
    
    def form_valid(self, form):
        category = form.save(commit=False)
        category.organization = self.request.user.userprofile
        category.save()
        return super(CategoryCreateView, self).form_valid(form)
    
class CategoryUpdateView(OrganizerAndLoginRequiredMixin, generic.UpdateView):
    template_name = 'categories/category_update.html'
    form_class = CreateCategoryForm
    context_object_name ='category'
        
    def get_success_url(self):
        return reverse('categories:category-list')
    
    def get_queryset(self):
        user = self.request.user
        
        if user.is_organizer:
            queryset = Category.objects.filter(organization = user.userprofile)
        else:
            queryset = Category.objects.filter(organization = user.agent.organization)
            
        return queryset

class CategoryDeleteView(OrganizerAndLoginRequiredMixin, generic.DeleteView):
    template_name = 'categories/category_delete.html'
    
    def get_success_url(self):
        return reverse('categories:category-list')
    
    def get_queryset(self):
        user = self.request.user
        
        if user.is_organizer:
            queryset = Category.objects.filter(organization = user.userprofile)
        else:
            queryset = Category.objects.filter(organization = user.agent.organization)
            
        return queryset
