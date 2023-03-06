from django.urls import path
from .views import AddView,StaffView,StaffProfilView,LogoutView,LoginView,InvitationView,EditView,staffremove,change_password
from .views import api_view,DetailStaffView,CreateStaffView

from . import views
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

# url partterns
urlpatterns = [
    path('',api_view, name = 'api_view'),
    # path('',StaffView.as_view(),name='staff'),
    path('add',AddView.as_view(), name='add_staff'),
    path('<id>/remove',staffremove, name='remove_staff'),
    path('logout',LogoutView.as_view(), name='logout'),
    path('login',LoginView.as_view(), name='login'),
    path("invitation/<id>",InvitationView.as_view(),name='invitation'),
    path("edit/<pk>",EditView.as_view(),name="edit_staff"),
        path('token', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.RegisterView.as_view(), name='auth_register'),
   
        path('change-password',change_password,name="change_password"),
         path('api', views.getRoutes),

 path('<id>',StaffProfilView.as_view(),name="profil"),

]
