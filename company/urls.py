from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', views.company, name='company'),
    path('faq/', views.faq, name='faq'),
    path('add-kpi/', views.addKPI, name='add_kpi'),
]

