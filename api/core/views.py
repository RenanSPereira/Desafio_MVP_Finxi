from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Demanda
from .serializers import DemandaSerializer, DemandaCreateSerializer


# Create your views here.


class DemandaViewSet(viewsets.ModelViewSet):
    queryset = Demanda.objects.all()
    serializer_class = DemandaSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Demanda.objects.all()

        #mostra as demandas cadastradas pelo usuário logado
        return Demanda.objects.filter(anunciante=self.request.user.id)

    def create(self, request):
        serializer = DemandaCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        demanda = Demanda.objects.create(**serializer.data, anunciante=request.user)
        return Response(DemandaSerializer(demanda).data)
