from django.urls import path


from . import views
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

# url partterns
urlpatterns = [
    path('',views.staff,name='staff'),
    path('token', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('api', views.getRoutes),
    path("invitations/<id>",views.invitation,name='invitation'),
    path("invitations",views.invitations,name="invitations"),

    path('<id>',views.staffmember,name="profil"),
 
    



]
