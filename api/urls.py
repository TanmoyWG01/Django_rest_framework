from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.studentsVieW),
    path('students/<int:pk>/', views.studentDetailView),
]  