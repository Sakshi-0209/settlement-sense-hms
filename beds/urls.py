from django.urls import path
from . import views

urlpatterns = [

    path(
        "",
        views.bed_list,
        name="beds",
    ),

    path(
        "add/",
        views.add_bed,
        name="add_bed",
    ),

    path(
        "view/<int:pk>/",
        views.view_bed,
        name="view_bed",
    ),

    path(
        "edit/<int:pk>/",
        views.edit_bed,
        name="edit_bed",
    ),

    path(
        "delete/<int:pk>/",
        views.delete_bed,
        name="delete_bed",
    ),

]