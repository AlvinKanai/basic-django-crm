from django import forms
from .models import Lead, Agent


class LeadModelForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = (
            'first_name',
            'last_name',
            'email',
            'phone',
            'agent',
            'category',
        )

class AssignAgentForm(forms.Form):
    agent = forms.ModelChoiceField(queryset=Agent.objects.none())
    
    def __init__(self,*args, **kwargs):
        request = kwargs.pop('request')
        agents = Agent.objecs.filter(organization = request.user.userprofile)
        # updating agent in the choice field based on agents from the organisation
        super(AssignAgentForm, self).__init__(*args, **kwargs)
        self.fields['agent'].queryset = agents