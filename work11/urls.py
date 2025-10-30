from django.urls import path
from . import views

app_name = "work11"

urlpatterns = [
    path("simple_qa/", views.simple_qa, name="simple_qa"),
]
