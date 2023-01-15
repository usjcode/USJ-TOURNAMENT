from django.contrib import admin
from django.urls import path
from .views import AboutView,AddView,HomeView,AddCCL1IView

urlpatterns = [
    path('',HomeView.as_view(),name='candidate'),
    path('about',AboutView.as_view()),
    path('add',AddView.as_view(), name='choice_add_candidate'),
    path('add/CCL1I',AddCCL1IView.as_view(), name='add_candidate'),

]
