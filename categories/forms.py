from django import forms
from leads.models import Lead, Category

class LeadCategoryUpdateForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = (
            'category',
        )
        
        
class CreateCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = (
            'name',
        )
        