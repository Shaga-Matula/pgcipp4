from .views import firstpage
from django.urls import path

urlpatterns = [
    path('', firstpage, name="home"),
]
