from main.models import Todo, Usera
from main.serializer import TodoSerializer, UseraSerializer
from rest_framework import generics
# from rest_framework.permissions import IsAuthenticated

# Create your views here.
class TodoListView(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    # permission_classes = [IsAuthenticated]

class TodoCreateView(generics.CreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class TodoRetrieveView(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class TodoUpdateView(generics.UpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class TodoDestroyView(generics.DestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class UseraCreateView(generics.CreateAPIView):
    queryset = Usera.objects.all()
    serializer_class = UseraSerializer