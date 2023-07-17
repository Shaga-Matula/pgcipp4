from .import views
from django.urls import path
from .views import student_creation, kyu_creation_view


urlpatterns = [
    path('', views.firstpage.as_view(), name="home"),
    path('success_page/', views.success_page, name='success'),
    path('student_creation/', views.student_creation, name='student_creation'),
    path('kyu_creation/', views.kyu_creation_view, name='kyu_creation'),
    path('student_get/', views.student_list, name='student_get'),
    path('edit_record/<int:Student_ID>/', views.edit_record, name='edit_record'),
    
]

