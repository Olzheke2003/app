from django.contrib import admin
from django.urls import path, include
from .views import UserLoginView

urlpatterns = [
    path('Login/', UserLoginView.as_view(), name='login'),
]
