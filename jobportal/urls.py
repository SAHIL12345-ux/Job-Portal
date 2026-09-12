"""
URL configuration for jobportal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from jobs.views import home
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('', include('jobs.urls')),
]
