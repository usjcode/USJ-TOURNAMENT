from django.shortcuts import render,redirect
from .models import Tournament
from candidate.models import Candidacy
from django.views.generic import TemplateView
from django.views import View
from django.views.generic.edit import FormView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.functions import Now
from rest_framework.parsers import JSONParser
import datetime
from .forms import UpdateTournamentForm
from rest_framework import status

from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .serializer import TournamentSerializer,TournamentCandidateSerializer



class Updateview(UpdateView):
    template_name = 'add_tournament.html'
    model = Tournament
    form_class = UpdateTournamentForm
    success_url='/'



@api_view(['POST','GET','DELETE'])
def tournaments(request):

    if request.method == 'POST':
        # data= JSONParser().parse(request)
        serializer = TournamentSerializer(data=request.data)
        if serializer.is_valid():
            if(Tournament.objects.filter(type=request.data["type"]).exists()):
                return Response({},status=status.HTTP_204_NO_CONTENT)
            else:
                serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) 
        else:
            return Response(serializer.errors,status=status.HTTP_200_OK)
        
    elif request.method == 'GET':
        tournaments= Tournament.objects.all()
        serializer = TournamentSerializer(tournaments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        tournaments = Tournament.objects.all()
        tournaments.delete()
        return JsonResponse({}, status=status.HTTP_204_NO_CONTENT)

@api_view(['PATCH','GET','DELETE'])
def tournament(request,id):
    tournament=Tournament.objects.get(id=id)
    if request.method=="GET":
        serializer=TournamentSerializer(tournament)
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    elif request.method=="DELETE":
        tournament.delete()
        return JsonResponse({}, status=status.HTTP_201_CREATED)
    elif request.method == 'PATCH':
        data= JSONParser().parse(request)
        serializer = TournamentSerializer(tournament,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED) 
        else:
            return Response(serializer.errors,status=status.HTTP_200_OK)
    
    

@api_view(['PATCH','GET','DELETE'])
def tournamentcandidates(request,id):
    candidates=Candidacy.objects.filter(tournament_id=id)
    if request.method=="GET":
        serializer=TournamentCandidateSerializer(candidates,many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    


@api_view(['POST','GET'])
def tournamentsubjets(request,id):
    pass


    
