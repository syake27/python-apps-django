from django.urls import path
from . import views

app_name = "work05"

urlpatterns = [
    path("index/", views.index, name="index"),
    path("profile/", views.profile, name="profile"),
]
