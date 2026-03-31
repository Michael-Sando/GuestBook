from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("entries/", views.entry_list, name="entry_list"),
]