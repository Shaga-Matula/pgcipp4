from .import views
from django.urls import path
from .views import student_creation



urlpatterns = [
    path('', views.firstpage.as_view(), name="home"),
    path('success_page/', views.success_page, name='success'),
    path('student_creation/', views.student_creation, name='student_creation'),
]

