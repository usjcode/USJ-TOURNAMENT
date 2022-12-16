from django.contrib import admin
from django.urls import path
from .views import AboutView,AddView,HomeView

urlpatterns = [
    path('',HomeView.as_view(),name=''),
    path('about',AboutView.as_view()),
    path('add',AddView.as_view(), name='add_candidate'),

]
