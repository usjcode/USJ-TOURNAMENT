from django.urls import path
from .views import AddView,StaffView,StaffProfilView,LogoutView,LoginView,InvitationView


# url partterns
urlpatterns = [
    path('',StaffView.as_view(),name='staff'),
    path('add',AddView.as_view(), name='add_staff'),
    path('logout',LogoutView.as_view(), name='logout'),
    path('login',LoginView.as_view(), name='login'),
    path("invitation/<id>",InvitationView.as_view(),name='invitation'),
    path('<id>',StaffProfilView.as_view(),name="profil"),
    



]
