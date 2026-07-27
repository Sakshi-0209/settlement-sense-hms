from django.urls import path
from . import views

urlpatterns = [

    path(
        "",
        views.admission_list,
        name="admissions",
    ),

    path(
        "add/",
        views.add_admission,
        name="add_admission",
    ),

    path(
        "view/<int:pk>/",
        views.view_admission,
        name="view_admission",
    ),

    path(
        "edit/<int:pk>/",
        views.edit_admission,
        name="edit_admission",
    ),

    path(
        "delete/<int:pk>/",
        views.delete_admission,
        name="delete_admission",
    ),

]