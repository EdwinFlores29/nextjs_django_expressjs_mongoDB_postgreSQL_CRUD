from rest_framework import serializers 
from .models import Task

class TaskSerializer(serializers.ModelSerializer): #aca se hace llamado a las clases
    class Meta: # en que model se esta basando, el modelo es Task, de models.py class Task
        model = Task
        fields = ('id', 'title', 'description', 'done', 'created_at') #aca los campos que se utilizan de un dato de python a un dato json
        read_only_fields = ('id', 'created_at') # campos que no se necesitan modificar por el uso de read_only_fields