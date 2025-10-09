from django.urls import path
from . import views

app_name = "work09"

urlpatterns = [
    path("", views.todo_list, name="todo_list"),
    path("create/", views.todo_create, name="todo_create"),
]
