from rest_framework import generics

from .models import Task
from .serializers import TodoSerializer

class TodoListAPI(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TodoSerializer

class TodoCreateAPI(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TodoSerializer

class TodoUpdateAPI(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TodoSerializer

class TodoDeleteAPI(generics.DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TodoSerializer

