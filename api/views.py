from candy.models import Candy
from rest_framework import viewsets, filters, generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CandySerializer

# Create your views here.


class GetAllCandy(generics.ListAPIView):
    serializer_class = CandySerializer
    queryset = Candy.objects.all()
