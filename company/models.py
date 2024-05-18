from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=40)
    pitch = models.TextField(max_length=150)
    address = models.TextField()
    location = models.TextField()
    county = models.TextField()
    country = models.TextField()
    phone = models.CharField(max_length=40)
    email = models.EmailField()
    
    def __str__(self):
        return self.name

class CompanyBranch(models.Model):
    branch_name = models.CharField(max_length= 200)
    branch_address = models.TextField(max_length= 500)
    location = models.CharField(max_length= 200)
    region = models.CharField(max_length= 200)
    country = models.CharField(max_length= 200)

    def __str__(self):
        return self.branch_name
    
class KeyPerfomanceIndicator(models.Model):
    KPI_name = models.CharField(max_length = 200)
    KPI_defination = models.TextField(max_length=500)
    why_is_it_important = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.KPI_name

class Product(models.Model):
    product_name = models.CharField(max_length=350)
    product_price = models.FloatField(default=0)
    def __str__(self):
        return self.product_name
    
class FrequentlyAskedQuestion(models.Model):
    question = models.CharField(max_length=350)
    answer = models.TextField(max_length= 1000)

    def __str__(self):
        return self.question
    