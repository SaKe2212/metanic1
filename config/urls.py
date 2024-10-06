from sys import meta_path

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('met/', include('met.urls')),



]


