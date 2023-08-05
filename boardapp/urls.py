from django.urls import path, include
from .views import signupfunc, loginfunc, listfunc

urlpatterns = [
    path('signup/', signupfunc),
    path('login/', loginfunc),
    path('list/', listfunc)
]
