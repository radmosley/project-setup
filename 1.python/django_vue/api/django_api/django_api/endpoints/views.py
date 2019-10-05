# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
import json

from .models import endPoint1
from .serializers import EndPointSerializer
from rest_framework import generics

# Create your views here.
def index(request):
    name = request.GET.get('name')
    return HttpResponse("<h1>Hi</h1"+str(name))

class endPointsList(generics.ListCreateAPIView):
    queryset = endPoint1.objects.all()
    serializer_class = EndPointSerializer

class endPointsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = endPoint1.objects.all()
    serializer_class = EndPointSerializer