
from django.urls import path

from . import views
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    
    path("<id>",views.candidate,name="candidate"),
    path("",views.candidates,name="candidates"),


    
]
