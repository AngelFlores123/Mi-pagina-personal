from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home),
    path('RSA_public_key/', views.RSA_public_key),
]