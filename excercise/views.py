from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import ExcerciseSerializer
from .models import Excercise

class ExcerciseViewset(viewsets.ModelViewSet):
    queryset = Excercise.objects.all()
    serializer_class = ExcerciseSerializer
