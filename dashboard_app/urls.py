from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('sign_in', views.sign_in_render)
]