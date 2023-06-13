from django.urls import path


from . import views
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

from django.contrib.auth import views as auth_views

# url partterns
urlpatterns = [
    path('',views.staff,name='staff'),
    path('token', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('api', views.getRoutes),
    path("invitations/<id>",views.invitation,name='invitation'),
    path("invitations/<id>/validation",views.invitationvalidation,name='invitation'),

    path("invitations",views.invitations,name="invitations"),
    path("invitations",views.invitations,name="invitations"),

    path('<id>',views.staffmember,name="profil"),
 
    
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    path('password_reset_send/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_send.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_form.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_done.html'), name='password_reset_complete')


]
