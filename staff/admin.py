from django.contrib import admin
from . models import Staff, StaffGroup, Pipeline, Target, Report, PipelineNotes

# Register your models here.

admin.site.register(StaffGroup)
admin.site.register(Staff) 
admin.site.register( Pipeline) 
admin.site.register(Target) 
admin.site.register(Report) 
admin.site.register(PipelineNotes)
