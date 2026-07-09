from django.urls import path
from . import views

urlpatterns = [

    path(
        "",
        views.ward_list,
        name="wards",
    ),

    path(
        "add/",
        views.add_ward,
        name="add_ward",
    ),

    path(
        "view/<int:pk>/",
        views.view_ward,
        name="view_ward",
    ),

    path(
        "edit/<int:pk>/",
        views.edit_ward,
        name="edit_ward",
    ),

    path(
        "delete/<int:pk>/",
        views.delete_ward,
        name="delete_ward",
    ),

]