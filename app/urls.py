from django.contrib import admin
from django.urls import path, include
from recruitment_agency.views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('jobs/', include('browse_job.urls'), name='jobs'),
    path('', include('users.urls')),
]
