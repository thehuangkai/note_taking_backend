from django.shortcuts import render
from .models import Todo
from rest_framework import generics
from .serializers import TodoSerializer

class TodoCreate(generics.CreateAPIView):
    queryset = Todo.objects.all(),
    serializer_class = TodoSerializer

class TodoList(generics.ListAPIView):
    serializer_class = TodoSerializer
    model = serializer_class.Meta.model


    def get_queryset(self):
        queryset = self.model.objects.all()
        completed = self.request.query_params.get('completed')
        if completed is not None:
            queryset = queryset.filter(completed=completed)
        return queryset.order_by('-created_at')



class TodoDetail(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class TodoUpdate(generics.RetrieveUpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class TodoDelete(generics.RetrieveDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

