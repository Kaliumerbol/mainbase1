from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from mainbase1.models import Mainbase1
from mainbase1.serializers import Mainbase1Serializer
from rest_framework import views, generics

# Это сокращение
class Mainbase1ListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, ]
    queryset = Mainbase1.objects.all()
    serializer_class = Mainbase1Serializer
# Это сокращение
class Mainbase1DetailUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, ]
    queryset = Mainbase1.objects.all()
    serializer_class = Mainbase1Serializer
    lookup_field = 'id'