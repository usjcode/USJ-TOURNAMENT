from django.shortcuts import render,redirect
from .models import OralNote, Tournament,Candidacy, WritingNote
from django.views import View
from django.views.generic.edit import FormView,UpdateView
from django.db.models.functions import Now
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.decorators import api_view
import datetime
from .serializer import CandidateSerializer, OralNoteSerializer, WritingNoteSerializer
from rest_framework.response import Response

from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from rest_framework import status    

@api_view(['DELETE','GET'])
def candidate(request,id):
    candidate=Candidacy.objects.get(id=id)
    if request.method=="GET":
        serializer=CandidateSerializer(candidate)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)
    if request.method=="DELETE":
        candidate.delete()
        return JsonResponse({}, status=status.HTTP_201_CREATED)
    

@api_view(['DELETE','GET','POST'])
def candidates(request):
    candidates=Candidacy.objects.all()
    if request.method=="POST":
        data= JSONParser().parse(request)
        serializer = StaffInvitationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data, status=status.HTTP_201_CREATED) 

    if request.method=="GET":
        serializer=CandidateSerializer(candidates,many=True,context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method=="DELETE":
        candidate.delete()
        return Response({}, status=status.HTTP_200_OK)
    
@api_view(['GET','POST'])
def candidateoralnote(request,tournamentid,anonymat):
    if request.method=="GET":
        tournament=Tournament.objects.get(id=tournamentid)
        candidate=Candidacy.objects.get(anonymat_number=anonymat,tournament=tournament)
        note=OralNote.objects.get(candidate=candidate)
        serializer=OralNoteSerializer(note,context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method=="POST":
        data= JSONParser().parse(request)

        serializer = WritingNoteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data, status=status.HTTP_201_CREATED) 


@api_view(['GET','POST'])
def candidatewritingnotes(request,tournamentid,anonymat):
    if request.method=="GET":
        tournament=Tournament.objects.get(id=tournamentid)
        candidate=Candidacy.objects.get(anonymat_number=anonymat,tournament=tournament)
        
        note=WritingNote.objects.filter(candidate=candidate)
        serializer=WritingNoteSerializer(note,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method=="POST":
        data= JSONParser().parse(request)
        serializer = OralNoteSerializer()(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data, status=status.HTTP_201_CREATED) 

    
    

    

class AddView(FormView):

    def form_valid(self, form):
        candidat=form.save(commit=False)
        type=self.kwargs["tournament"]
        print(type)
        tournament=Tournament.objects.filter(date_inscription__gt=Now(),type=type).first()
        candidat.tournament=tournament
        candidat.save()
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        print(self.kwargs["tournament"])
        context['c'] = Tournament.objects.filter(date_inscription__gt=Now(),type=self.kwargs["tournament"]).exists()
        context['type']=self.kwargs["tournament"]
        print(context['c'])
        return context


class Updateview(UpdateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id=self.kwargs['pk']
        candidate=Candidacy.objects.get(pk=id)
        context['c'] =True
        if datetime.date.today() >=candidate.tournament.date_debut:
            context['c'] =False
        return context
    
    

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class Updatetournamentview(LoginRequiredMixin,View):
        def get(self, request, *args, **kwargs):
            id=kwargs["pk"]
            tournamentname=kwargs["tournament"]
            candidat=Candidacy.objects.get(id=id)
            exist=Tournament.objects.filter(date_inscription__gt=Now(),type=tournamentname).exists()
            success=False
            if exist:
                tournament=Tournament.objects.filter(date_inscription__gt=Now(),type=tournamentname).first()
                candidat.tournament=tournament
                candidat.save()
                success=True
                return redirect("candidate")
                
            return  render(request,"updatecandidatetournament.html",context={"success":success})

    
    
    
    



