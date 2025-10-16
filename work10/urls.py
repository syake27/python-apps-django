from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "work10"

urlpatterns = [
    path("", views.todo_list, name="todo_list"),
    path("create/", views.todo_create, name="todo_create"),
    path("edit/<int:pk>/", views.todo_edit, name="todo_edit"),
    path("toggle/<int:pk>/", views.todo_toggle, name="todo_toggle"),
    path("delete/<int:pk>/", views.todo_delete, name="todo_delete"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="work10/login.html"),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(next_page="work10:login"),
        name="logout",
    ),

    path("register/", views.register, name="register"),
]
