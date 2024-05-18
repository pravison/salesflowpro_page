from django.urls import path
from . import views

urlpatterns = [
    path('', views.customers, name='customers'),
    path('leads/', views.leads, name='leads'),
    path('<int:id>/add_customer_note', views.addCustomerNotes, name='add_customer_note'),
    path('customer/<int:id>/', views.viewCustomer, name='customer'),
    path('customer/add/', views.addCustomer, name='add_customer'),
    path('<int:id>/edit/', views.editCustomer, name='edit_customer'),
    path('interactions/', views.interactions, name='interactions'),
    path('interactions/<int:id>/view/', views.view_interaction, name='view_interaction'),
    path('interactions/add/', views.addInteraction, name='add_interaction'),
    path('interactions/<int:id>/add/', views.addCustomerInteraction, name='add_customer_interaction'),
    path('add_product/<int:id>/', views.addProduct, name='add_product'),
    path('add_label/<int:id>/', views.addLabel, name='add_label'),
    path('add_product_to_customer/<int:id>/', views.addCustomerProduct, name='add_product_to_customer'),
    path('add_label_to_customer/<int:id>/', views.addCustomerLabel, name='add_label_to_customer'),
    path('self_add/', views.CustomerSelfAdd, name='customer_self_add'),

]

