from django import forms 
from django.db import models
from django.forms import ModelForm
from . models import Pipeline, Target, Report
from customers.models import Customer
from tempus_dominus.widgets import DateTimePicker

# class CustomDateTimeField(forms.DateTimeField):
# 	def __init__(self, *args, **kwargs):
# 		kwargs.setdefault('widget', DateTimePicker(options={'format': 'DD-MM-YYYY HH:mm', 'class':'form-control', 'useCurrent':True, 'collapse':False,}))
# 		super().__init__( *args, **kwargs)

class AddPipelineForm(ModelForm):
	customer = forms.ModelChoiceField(queryset=Customer.objects.all(), widget=forms.TextInput(attrs={'class': 'searchable-customer-list form-control'}))
	class Meta:
		model = Pipeline
		fields = ('task', 'important', 'customer', 'what_to_expect', 'notes', 'pipeline_date', 'pipeline_time', 'done')
		widgets = {
			"task": forms.TextInput(attrs={'class': "form-control", 'placeholder': 'whats your task', 'id': 'task'}),
			"important" :forms.CheckboxInput(attrs={ 'placeholder': 'important', 'id': 'important'}),
			#"customer": forms.Select(attrs={'class': "company-customer form-control"}),
			"what_to_expect": forms.Textarea(attrs={'class': "form-control", 'placeholder': 'what are your expectations', 'id': 'what_to_expect'}),
			"notes": forms.Textarea(attrs={'class': "form-control", 'placeholder': 'add some notes', 'id': 'notes'}),
			"pipeline_date": forms.DateInput(attrs={'class': "form-control", 'type':'date', 'placeholder': 'date to be done', 'id': 'pipeline_date'}),
		    "pipeline_time": forms.TimeInput(attrs={'class': "form-control", 'type':'time', 'placeholder': 'date to be done', 'id': 'pipeline_time'}) ,
			"done": forms.CheckboxInput(attrs={ 'placeholder': 'important', 'id': 'important'})}


class AddTargetForm(ModelForm):
	class Meta:
		model = Target
		fields = ('timeline', 'KPI', 'target', 'notes')
		widgets = {
			"timeline": forms.Select(attrs={'class': "form-control", 'placeholder': 'timeline', 'id': 'timeline'}),
			"KPI" :forms.Select(attrs={'class': "form-control", 'placeholder': 'KPI', 'id': 'KPI'}),
			"target": forms.NumberInput(attrs={'class':"form-control", 'placeholder': "target"}),
			"notes": forms.Textarea(attrs={'class': "form-control", 'placeholder': 'target notes'}),
		}
		
class AddReportForm(ModelForm):
	class Meta:
		model = Report
		fields = ('target', 'achieved', 'notes')
		widgets = {
			"target": forms.Select(attrs={'class': "form-control", 'placeholder': 'target'}),
			"achieved" :forms.NumberInput(attrs={'class': "form-control", 'placeholder': 'achieved', }),
			"notes": forms.Textarea(attrs={'class': "form-control", 'placeholder': 'add some notes'})
			}
		
	def __init__(self, *args, **kwargs):
		user = kwargs.pop('user', None)
		super(AddReportForm, self).__init__(*args, **kwargs)
		if user:
			self.fields['target'].queryset = Target.objects.filter(created_by=user , report=None)
			
