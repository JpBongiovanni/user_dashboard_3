from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('sign_in', views.sign_in_render),
    path('register', views.register_render),
    path('admin_dashboard_render', views.admin_dashboard_render),
    path('user_information_render', views.user_information_render)
]