
import random
import string

from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import redirect ,render
from .models import StaffInvitation,StaffUser
from django.core.mail import send_mail
from django.contrib.auth import update_session_auth_hash
from rest_framework import status
from rest_framework.parsers import JSONParser


from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import StaffInvitationSerializer,MyTokenObtainPairSerializer, StaffSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics


#############-- --########
from django.contrib import messages
from django.contrib.auth.forms import ReinitialiserMdpForm
from django.contrib.auth import views as auth_views



def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer



@api_view(['GET','DELETE'])
def staffmember(request,id):
    staffmember=StaffUser.objects.get(id=id)
    if request.method=="GET":
        serializer=StaffSerializer(staffmember)

        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    if request.method=="DELETE":
        staffmember.delete()
        return JsonResponse({}, status=status.HTTP_201_CREATED)



@api_view(['POST','GET','DELETE'])
def invitations(request):

    if request.method == 'POST':
        data= JSONParser().parse(request)
        staff_serializer = StaffInvitationSerializer(data=data)
        if staff_serializer.is_valid():
            staff_serializer.save()
            mail = staff_serializer.data.get('email')
            id= staff_serializer.data.get('id')

                    
            send_mail("INVITATION POUR L'UTILISATION DU LOGICIEL DE GESTION DE CONCOURS DE USJ",
                'Veuiller cliquez ici pour active votre compte utilisateur localhost:3000/staff/invitations/{}/validation'.format(id),
                'TON ADDRESSE MAIL',
                [mail],
                fail_silently=False
            )
            return Response(data, status=status.HTTP_201_CREATED) 
        else:
            return Response(staff_serializer.errors,status=status.HTTP_201_CREATED)
        
    elif request.method == 'GET':
        invitations = StaffInvitation.objects.all()
        serializer = StaffInvitationSerializer(invitations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        invitations = StaffInvitation.objects.all()
        invitations.delete()
        return JsonResponse({}, status=status.HTTP_204_NO_CONTENT)

@api_view(['PATCH','GET','DELETE'])
def invitation(request,id):
    invitation=StaffInvitation.objects.get(id=id)
    if request.method  =='PATCH':
        data= JSONParser().parse(request)
        serializer = StaffInvitationSerializer(invitation,data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED) 
        else:
            return Response(serializer.errors,status=status.HTTP_200_OK)
    if request.method =='DELETE':
        invitation = StaffInvitation.objects.get(id=id)
        invitation.delete()
        return JsonResponse({}, status=status.HTTP_204_NO_CONTENT)
    if request.method == 'GET':
        

        serializer=StaffInvitationSerializer(invitation)
        return JsonResponse(serializer.data,status=status.HTTP_200_OK)

@api_view(['GET'])
def invitationvalidation(request,id):
    invitation=StaffInvitation.objects.get(id=id)
    randompassword=get_random_string(8)
    name="utilisateur"+str(invitation.id) 
    lastuser=StaffUser.objects.last()  
     
    newuser:StaffUser
    if invitation.active:
        newuser=StaffUser(username="user"+str(lastuser.id+1 or 0),email=invitation.email,role=invitation.role,name=name)
        newuser.set_password(randompassword)
        newuser.save()     
        invitation.active=False
        invitation.validate=True
        invitation.save()
    return Response(request.data,status=status.HTTP_200_OK)

    
@api_view(['GET','DELETE','POST'])
def staff(request):
    if request.method=="DELETE":
        staff=StaffUser.objects.all()
        staff.delete()
        return Response({},status=status.HTTP_200_OK)

    elif request.method=="GET":
        staff=StaffUser.objects.all()
        serializer=StaffSerializer(staff,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/token/',
        '/token/refresh/',
        '/staff/',
        '/staff/<id>'

    ]
    return Response(routes)





#############--def--#############

def reinitialiser_mdp(request):
    if request.method == 'POST':
        form = ReinitialiserMdpForm(request.POST)
        if form.is_valid():
            form.save(request=request)
            messages.success(request, 'Un email a été envoyé avec des instructions pour réinitialiser votre mot de passe.')
            return redirect('reinitialiser_mdp_done')
        else:
            form = ReinitialiserMdpForm()
            return render(request, 'reinitialiser_mdp.html',{'form':form})
        



# @api_view(['GET'])
# def changePassword(request):
    