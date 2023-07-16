from .import views
from .views import student_creation
from django.urls import path
from .views import CreateStudent



urlpatterns = [
    path('', views.firstpage.as_view(), name="home"),
    path('success_page/', views.success_page, name='success'),
    path('student_creation/', views.student_creation, name='Student Creation'),
]