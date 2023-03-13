
from django.urls import path

from . import views
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    
    path("deleteStudent/<id>",views.deleteview,name="deleteStudent"),
    
]
