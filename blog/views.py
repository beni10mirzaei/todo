from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from .models import *
from .serializers import *

class TodoList(ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class TodoCreate(CreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class TodoDetail(RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class TodoUpdate(UpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class TodoDelete(DestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

