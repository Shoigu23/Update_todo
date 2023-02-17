from rest_framework.serializers import ModelSerializer
from main.models import Todo, Usera

class TodoSerializer(ModelSerializer):
    class Meta:
        model = Todo
        fields = ('title','description')

class UseraSerializer(ModelSerializer):
    class Meta:
        model = Usera
        fields = ('first_name', 'last_name', 'age', 'email')