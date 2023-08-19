from django.urls import path
from . import views

urlpatterns=[
    path('norwegianwood/',views.norwegian_wood),
    path('turingpaper/', views.turing_paper, name='turing_paper'),
    path('psych/', views.psych, name='psych')

]