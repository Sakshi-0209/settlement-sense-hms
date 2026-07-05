from django.urls import path
from . import views

urlpatterns = [

    path("", views.patient_list, name="patients"),

    path(
        "add/",
        views.add_patient,
        name="add_patient",
    ),

]