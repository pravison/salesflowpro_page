from django.urls import path
from . import views

urlpatterns = [
    path('', views.pipeline, name='pipeline'),
    path('important/', views.importantPipeline, name='important_pipeline'),
    path('pipeline/<int:id>/', views.view_pipeline, name='view_pipeline'),
    path('<int:id>/add_pipeline_note', views.addPipelineNotes, name='add_pipeline_note'),
    path('customer-autocomplete/', views.CustomerAutocomplete, name='customer-autocomplete'),
    path('<int:id>/edit_pipeline_done/', views.edit_pipeline_done, name='edit_pipeline'),
    path('<int:id>/resechedule/', views.edit_pipeline_resechedule, name='resechedule'),
    path('<int:id>/edit/', views.edit_pipeline, name='edit'),
    path('add-pippeline', views.addPipeline, name='add_pipeline'),
    path('staffs/', views.staffs, name='staffs'),
    path('staffs/<int:id>/view', views.ViewStaff, name='view_staff'),
    path('add-staff', views.addStaff, name='add_staff'),
    path('add-report', views.addReport, name='add_report'),
    path('add-target', views.addTarget, name='add_target'),

]

