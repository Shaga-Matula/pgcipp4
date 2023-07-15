from . import views
from django.urls import path
from .views import create_student_lvl

urlpatterns = [
    path('', views.firstpage.as_view(), name="home"),
    path('create-student-lvl/', create_student_lvl, name='create_student_lvl'),
]

