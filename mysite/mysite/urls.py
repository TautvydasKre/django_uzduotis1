from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('cars/', include('autoservisas.urls')),
    path('admin/', admin.site.urls),
]