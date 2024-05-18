from django.contrib import admin
from . models import Customer, CustomerLabel, ProbableConversationOutcome, ProbableNextStep, Interaction, CustomerAgents, Note

# Register your models here.

admin.site.register(Customer)
admin.site.register(CustomerLabel)
admin.site.register(ProbableConversationOutcome)
admin.site.register(ProbableNextStep)
admin.site.register(Interaction)
admin.site.register(CustomerAgents)
admin.site.register(Note)




