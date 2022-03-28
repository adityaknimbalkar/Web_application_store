from unicodedata import name
from django.contrib import admin
from django.urls import path
from hello import views

urlpatterns = [
    path("", views.index, name='home'),
    path("app", views.tasks, name="apps"),
    path("info", views.infos, name="infos"),
    path("id", views.app_byid, name="appdata")


]
