from django.urls import path
from . import views

urlpatterns = [

    path("", views.appointment_list, name="appointments"),

    path("add/", views.add_appointment, name="add_appointment"),

    path("view/<int:pk>/", views.view_appointment, name="view_appointment"),

    path("edit/<int:pk>/", views.edit_appointment, name="edit_appointment"),

    path("delete/<int:pk>/", views.delete_appointment, name="delete_appointment"),

]