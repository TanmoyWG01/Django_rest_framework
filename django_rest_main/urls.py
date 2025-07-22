from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    # Web application endpoints
    path('students/', include('students.urls')),

    # API endpoints
    path('api/v1/', include('api.urls')),
]
