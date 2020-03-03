from django.shortcuts import render
from rest_framework import generics
from api.serializers import RockDetailSerializer
# Create your views here.
class RockCreate(generics.CreateAPIView):
    serialazer_class = RockDetailSerializer

