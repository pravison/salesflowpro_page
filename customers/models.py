from django.db import models
from datetime import date
from django.contrib.auth.models import User
from company.models import CompanyBranch, Product
# Create your models here.
LEAD_TYPE_CHOICES = {
    ("hot", "hot"),
    ("warm", "warm"),
    ("cold", "cold"),
}

CONVERSATION_METHOD_CHOICES = {
    ("call", "call"),
    ("chat", "chat"),
    ("face", "face to face "),

}

COLOUR_CHOICES = {
    ("primary", "blue"),
    ("secondary", "grey"),
    ("success", "green "),
    ("danger", "red"),
    ("warning", "yellow"),
    ("info", "sky blue "),
    ("dark", "black"),
    ("white", "white "),

}

class CustomerLabel(models.Model):
    label = models.CharField(max_length=100)
    colour = models.CharField(max_length=70, choices=COLOUR_CHOICES , default="primary")
    definition = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.label
    
class Customer(models.Model):
    name = models.CharField(max_length=350)
    phone = models.CharField(max_length=17)
    phone1 = models.CharField(max_length=17, null=True, blank=True)
    email = models.EmailField(blank=True, null=True)
    location = models.CharField(max_length=250)
    added_by = models.ForeignKey(User, blank=True, null=True, on_delete=models.DO_NOTHING)
    label = models.ManyToManyField(CustomerLabel, blank=True)
    lead_type = models.CharField(max_length=20, choices=LEAD_TYPE_CHOICES)
    branch = models.ForeignKey(CompanyBranch, blank=True, null=True, on_delete=models.SET_NULL )
    product = models.ManyToManyField(Product, blank=True )
    description = models.TextField(max_length=1000, blank=True, null=True)
    active = models.BooleanField(default=False, help_text="set this true if an hot lead has converted to a customer")
    dormant = models.BooleanField(default=False, help_text="set this true if an active customer is dormant")
    date_added = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
    
class CustomerAgents(models.Model):
    customer = models.ForeignKey(Customer,  on_delete=models.CASCADE )
    agents = models.ManyToManyField(User)

    def __str__(self):
        return self.customer.name
    
class ProbableConversationOutcome(models.Model):
    name = models.CharField(max_length=150)
    colour = models.CharField(max_length=70, choices=COLOUR_CHOICES , default="primary")

    def __str__(self):
        return self.name
    
class ProbableNextStep(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name
class Note(models.Model):
    customer =  models.ForeignKey(Customer, null=True, blank=True, on_delete=models.DO_NOTHING )
    notes = models.TextField(max_length=1000, blank=True, null=True)
    added_by = models.ForeignKey(User, blank=True, null=True, on_delete=models.DO_NOTHING )
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.notes
    class Meta:
        ordering = ['-id']

class Interaction(models.Model):
    customer = models.ForeignKey(Customer, blank=True, null=True, on_delete=models.DO_NOTHING )
    staff = models.ForeignKey(User, blank=True, null=True, on_delete=models.DO_NOTHING )
    conversation_method = models.CharField(max_length=70, choices=CONVERSATION_METHOD_CHOICES)
    outcome = models.ForeignKey(ProbableConversationOutcome, blank=True, null=True, on_delete=models.DO_NOTHING)
    conversation_summary = models.TextField(max_length=1000, blank=True, null=True)
    next_step = models.ForeignKey(ProbableNextStep, blank=True, null=True,  on_delete=models.DO_NOTHING)
    what_to_expect = models.TextField(max_length=1000, blank=True, null=True)
    next_step_date = models.DateField()
    next_step_time = models.TimeField( blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer.name
    
    @property
    def is_past_due(self):
        return date.today() > self.next_step_date
    
    class Meta:
        ordering = ['-date_created']







