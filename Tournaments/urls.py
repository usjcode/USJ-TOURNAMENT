from django.contrib import admin
from django.urls import path

from candidate.views import candidateoralnote, candidatewritingnotes
from . import views

urlpatterns = [
    path('',views.tournaments, name = 'tournaments'),
    path('<int:id>',views.tournament),
    path('<int:id>/candidates',views.tournamentcandidates, name='add_tournament'),
    path('<tournamentid>/<anonymat>/oralnote',candidateoralnote,name="candidateoralnote"),
    path('<tournamentid>/<anonymat>/writingnote',candidatewritingnotes,name="candidatewritingnote")


]
