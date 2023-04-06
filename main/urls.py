from django.urls import path
from . import views
from .views import RegisterUser

urlpatterns = [
    path('', RegisterUser.as_view(), name='home'),
]