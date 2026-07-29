from django.urls import path
from . import views

urlpatterns = [

    path("", views.billing_list, name="billing"),

    path("add/", views.add_billing, name="add_billing"),

    path("view/<int:pk>/", views.view_billing, name="view_billing"),

    path("edit/<int:pk>/", views.edit_billing, name="edit_billing"),

    path("delete/<int:pk>/", views.delete_billing, name="delete_billing"),

]