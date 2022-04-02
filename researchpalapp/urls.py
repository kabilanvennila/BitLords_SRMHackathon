from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('file/',views.my_file,name="my_file"),
]