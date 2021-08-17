from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.writeview),
    path('result/', views.result),
]
