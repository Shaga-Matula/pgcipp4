from .import views
from .views import student_creation
from django.urls import path
<<<<<<< HEAD

=======
from .views import CreateStudent
>>>>>>> eb2f6c1777b1c543e023b76ec57259ad202f725f


urlpatterns = [
    path('', views.firstpage.as_view(), name="home"),
<<<<<<< HEAD
    path('success_page/', views.success_page, name='success'),
    path('student_creation/', views.student_creation, name='Student Creation'),
=======
    path('CreateStudent/', views.CreateStudent.as_view(), name="Create Student"),
>>>>>>> eb2f6c1777b1c543e023b76ec57259ad202f725f
]