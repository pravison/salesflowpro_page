from django.db import models
from django.contrib.auth.models import User
from company.models import CompanyBranch, KeyPerfomanceIndicator
from customers.models import Customer
# Create your models here.

TIMELINE_CHOICES = {
    ('Today', 'Today'),
    ('This Week', 'This Week'),
    ('This Month',  'This Month'),
    ('This Year', 'This Year')
}
class Staff(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    branch = models.ForeignKey(CompanyBranch, null=True, blank=True, on_delete = models.SET_NULL)
    role = models.CharField(max_length=200)
    phone = models.CharField(max_length=17, blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add = True)
    active = models.BooleanField(default=True)
    admin = models.BooleanField(default=False)

    def __str__(self):
        return f' {self.user.first_name}  {self.user.last_name}'
    
class StaffGroup(models.Model):
    group_name = models.CharField(max_length=200)
    staffs = models.ManyToManyField(Staff)
                                                                        
    def __str__(self):
        return self.group_name
    
    
class Target(models.Model):
    timeline = models.CharField(max_length=100, choices=TIMELINE_CHOICES, default="TODAY")
    KPI = models.ForeignKey(KeyPerfomanceIndicator, null=True, blank=True, on_delete=models.SET_NULL)
    target = models.IntegerField()
    notes = models.TextField(max_length=500, null=True, blank=True)
    created_by = models.ForeignKey(User,  null=True, blank=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{str(self.target)} - {self.KPI.KPI_name} for {self.timeline}'
    
    class Meta:
        ordering = ['-date_created']

class Pipeline(models.Model):
    task = models.CharField(max_length=150)
    important = models.BooleanField(default=False)
    customer = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.SET_NULL)
    what_to_expect = models.TextField(max_length=1000, blank=True, null=True)
    notes = models.TextField(max_length=5000, blank=True, null=True)
    pipeline_date = models.DateField()
    pipeline_time = models.TimeField(blank=True, null=True)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    done = models.BooleanField(default=False)
    postponed = models.BooleanField(default=False)
    postponed_counter=models.IntegerField(default=0)

    def __str__(self):
        return self.task
    
    class Meta:
        ordering = ['pipeline_date', 'pipeline_time']

class PipelineNotes(models.Model):
    pipeline = models.ForeignKey(Pipeline, on_delete=models.CASCADE)
    notes = models.TextField(max_length=5000)
    def __str__(self):
        return self.notes
    
    class Meta:
        ordering = ['id']


class Report(models.Model):
    target = models.ForeignKey(Target, null=True, blank=True, on_delete=models.SET_NULL)
    achieved = models.IntegerField()
    notes = models.TextField(max_length=500, null=True, blank=True)
    created_by = models.ForeignKey(User,  null=True, blank=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return f'target was {self.target.target} and  {self.achieved} was achieved'
    
    class Meta:
        ordering = ['-date_created']
