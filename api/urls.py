from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter 

router = DefaultRouter()
router.register('employees', views.EmployeeViewset, basename='employee')

urlpatterns = [
    # Route for functional api
    path('students/', views.studentsVieW),
    path('students/<int:pk>/', views.studentDetailView),

    # Route for class based api
    # path('employees/', views.Employees.as_view()),
    # path('employees/<int:pk>/', views.EmployeeDetail.as_view())

    # ViewSet
    path('', include(router.urls)),

    # nested serializers 
    path('blogs/', views.BlogsView.as_view()),
    path('comments/', views.CommentsView.as_view()),

    path('blogs/<int:pk>/', views.BlogDetailsView.as_view()),
    path('comments/<int:pk>/', views.CommentDetailsView.as_view()),
]  