from django.contrib import admin
from django.urls import path, include
from .views import BrowseJobView

app_name = 'jobs'

urlpatterns = [
    path('', BrowseJobView.as_view(), name='index'),
    path('Jobs/<int:category_id>', BrowseJobView.as_view(), name='category'),
]
