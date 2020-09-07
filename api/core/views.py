from django.shortcuts import render
from rest_framework import viewsets
from .models import Demanda
from .serializers import DemandaSerializer


# Create your views here.


class DemandaViewSet(viewsets.ModelViewSet):
    queryset = Demanda.objects.all()
    serializer_class = DemandaSerializer
