from django.shortcuts import render
from rest_framework import viewsets
from .models import Job
from .serializers import JobSerializer

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all().order_by('-id')
    serializer_class = JobSerializer

