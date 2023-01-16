from django.contrib import admin
from django.urls import path
from .views import AboutView,ChoiseAddView,HomeView,AddView,Updateview, deleteview
urlpatterns = [
    path('',HomeView.as_view(),name='candidate'),
    path('add/<tournament>',AddView.as_view(), name='add_candidate'),
    path('<pk>/update',Updateview.as_view(), name='update_candidate'),
    path('<id>/delete',deleteview, name='delete_candidate'),
    

]
