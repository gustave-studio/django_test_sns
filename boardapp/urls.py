from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.sSite.urls),
    path('', include('boardapp.urls')),
]
