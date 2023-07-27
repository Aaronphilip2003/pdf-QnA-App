from django.urls import path
from . import views

urlpatterns=[
    path('hello/',views.say_hello),
    path('',views.home),
    path('norwegianwood/',views.norwegian_wood),
    path('norwegian_wood', views.norwegian_wood, name='norwegian_wood'),

]