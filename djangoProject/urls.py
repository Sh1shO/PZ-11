from django.contrib import admin
from django.urls import path
from myFirstProject import views

urlpatterns = [
    path('', views.index),
    path('second/', views.second_page),
    path('1/', views.odin),
    path('2/', views.second_awdawdpage),
    path('3/', views.second_page),
    path('4/', views.second_page),
    path('5/', views.second_page),
]
