from django.urls import path
from . import views


urlpatterns = [
    path('', views.firstpage, name="home"),
]
