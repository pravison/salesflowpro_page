from django import forms 
from django.forms import ModelForm
from . models import Customer, CustomerLabel, CustomerAgents, ProbableConversationOutcome, ProbableNextStep, Note, Interaction
from tempus_dominus.widgets import DateTimePicker


class AddCustomerForm(ModelForm):
	class Meta:
		model = Customer
		fields = ('name', 'phone', 'phone1', 'email', 'location', 'label', 'lead_type', 'branch', 'product', 'description')
		widgets = {
			"name": forms.TextInput(attrs={'class': "form-control",  'id': 'name'}),
			"phone": forms.NumberInput(attrs={'class': "form-control", 'id': 'phone'}),
			"phone1": forms.NumberInput(attrs={'class': "form-control", 'id': 'phone1'}),
			"email": forms.EmailInput(attrs={'class': "form-control", 'id': 'email'}),
			"location": forms.TextInput(attrs={'class': "form-control", 'id': 'location'}),
			"label": forms.SelectMultiple(attrs={'class': "form-control", 'id': 'label'}),
			"lead_type": forms.Select(attrs={'class': "form-control", 'id': 'lead_type'}),
			"branch": forms.Select(attrs={'class': "form-control", 'id': 'branch'}),
			"product": forms.SelectMultiple(attrs={'class': "form-control", 'id': 'product'}),
			"description": forms.Textarea(attrs={'class': "form-control",  'id': 'description'}),
			}
		
class AddInteractionForm(ModelForm):
	class Meta:
		model = Interaction
		fields = ('customer', 'conversation_method', 'outcome', 'conversation_summary', 'next_step', 'what_to_expect', 'next_step_date', 'next_step_time')
		widgets = {
			"customer": forms.Select(attrs={'class': "form-control", 'id': 'customerInteraction'}),
			"conversation_method": forms.Select(attrs={'class': "form-control", 'id': 'conversationMethodInteraction'}),
			"outcome": forms.Select(attrs={'class': "form-control", 'id': 'outcomeInteraction'}),
			"next_step": forms.Select(attrs={'class': "form-control", 'id': 'nextStepInteraction'}),
			"what_to_expect": forms.Textarea(attrs={'class': "form-control",  'id': 'whatToExpectInteraction'}),
			"conversation_summary": forms.Textarea(attrs={'class': "form-control",  'id': 'conversationSummaryInteraction'}),
			"next_step_date": forms.TextInput(attrs={'class': "form-control ", 'type':"date", 'id': 'nextStepDateInteraction'}),
			"next_step_time": forms.TextInput(attrs={'class': "form-control ", 'type':"time" , 'id': 'nextStepTimeInteraction'}),
			}