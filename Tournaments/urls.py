from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.tournaments, name = 'tournaments'),
    path('<int:id>',views.tournament),
    # path('',HomeView.as_view(),name='home'),
    path('<int:pk>/candidates',views.tournamentcandidates, name='add_tournament'),

]
