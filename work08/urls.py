# work08/urls.py
from django.urls import path
from . import views

app_name = "work08"

urlpatterns = [
    path("", views.toppage, name="toppage"),
    path("new_memopage/", views.new_memopage, name="new_memopage"),
    path("memopage/<int:id>/", views.memopage, name="memopage"),
    path("memo_create/", views.memo_create, name="memo_create"),
    path("memo_update/<int:id>/", views.memo_update, name="memo_update"),
]
