from django.urls import path

# mon import pour la réinitialisation du mot de passe
from django.contrib.auth import views as auth_views

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
    
<<<<<<< Updated upstream
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    path('password_reset_send/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_send.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_form.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_done.html'), name='password_reset_complete')
=======
    
    #################--corps--####################
    
#     # path('reinitialiser_mdp/',auth_views.ReinitialiserMdpView.as_view(template_name="reinitialiser_mdp.html"),name="reinitialiser_mdp"),
#     path('reinitialiser_mdp/',views.reinitialiser_mdp,name="reinitialiser_mdp"),

#     path('reinitialiser_mdp_sent/',auth_views.ReinitialiserMdpDoneView.as_view(template_name="reinitialiser_mdp_sent.html"),name="reinitialiser_mdp_done"),
#     path('reinitialiser_mdp/<uid64>/<token>/',auth_views.ReinitialiserMdpConfirmationView.as_view(template_name="reinitialiser_mdp_form.html"),name="reinitialiser_mdp_confirmation"),
#     path('reinitialiser_mdp_complet/',auth_views.ReinitialiserMdpCompletView.as_view(template_name="reinitialiser_mdp_done.html"),name="reinitialiser_mdp_complet"),

# >>>>>>> Stashed changes


]
