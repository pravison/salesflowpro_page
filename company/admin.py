from django.contrib import admin
from . models import Company, CompanyBranch, Product, KeyPerfomanceIndicator, FrequentlyAskedQuestion

# Register your models here.
admin.site.register(Company)
admin.site.register(CompanyBranch)
admin.site.register(Product)
admin.site.register(KeyPerfomanceIndicator)
admin.site.register(FrequentlyAskedQuestion)

