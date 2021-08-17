from django.urls import path
from . import views

urlpatterns = [
    path('', views.writeview, name='write-page'),

]
