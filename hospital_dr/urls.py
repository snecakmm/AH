from django.urls import path
from . import views

urlpatterns = [
    path('', views.dr_home, name='dr_home'),
]

