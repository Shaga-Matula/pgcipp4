from . import views
from django.urls import path
from .views import CreateStudent


urlpatterns = [
    path('', views.firstpage.as_view(), name="home"),
    path('CreateStudent/', views.CreateStudent.as_view(), name="Create Student"),
]