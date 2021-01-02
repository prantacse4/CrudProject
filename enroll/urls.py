from django.contrib import admin
from django.urls import path
from enroll import views

urlpatterns = [
    path('', views.add_show, name="addshow"),
    path('delete/<int:id>/', views.delete, name="delete_data"),
    path('update/<int:id>/', views.update, name="update_data"),
]
