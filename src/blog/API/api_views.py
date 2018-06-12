from blog.models import *
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics

from . import serializers

class QuestionViewSet(viewsets.ModelViewSet):
    
    serializer_class = serializers.QuestionSerializer
    queryset = Question.objects.all()