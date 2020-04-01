from django.shortcuts import render
from rest_framework import viewsets
from . import serializers
from . import models


class TodoView(viewsets.ModelViewSet):
    serializer_class = serializers.TodoSerializer
    queryset = models.Todo.objects.all()
