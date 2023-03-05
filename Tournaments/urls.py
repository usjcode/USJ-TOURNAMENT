from django.contrib import admin
from django.urls import path
from .views import AboutView,AddView,HomeView,TournamentView,Updateview,deleteview,CreateTournamentView
from .views import DetailTournamentView
from .views import api_view

urlpatterns = [
    path('',api_view, name = 'api_view'),
    path('<int:pk>/', DetailTournamentView.as_view()),
    # path('',HomeView.as_view(),name='home'),
    path('about',AboutView.as_view()),
    path('add',AddView.as_view(), name='add_tournament'),
    path('<id>/delete',deleteview, name='delete_tournament'),
    path('<pk>/update',Updateview.as_view(), name='update_tournament'),
    path('tournament/<id>',TournamentView.as_view(), name='tournament'),
    path('create', CreateTournamentView.as_view()),
]
