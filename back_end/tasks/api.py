from rest_framework import viewsets, permissions
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet): # en restframework, un viewsets es un conjunto de vistas, este conjunto de vistas hace cada vez referencia cuando creamos una ruta, completa al CRUD, una vez sirve para put, get, post, y push
    queryset = Task.objects.all() # esta va a ser igual al tabla que va a importar en este caso Task
    permission_classes = [permissions.AllowAny] #para acceder a estas rutas, cualquiera puede acceder
    serializer_class = TaskSerializer #aqui utilizando un serializador 

    #ya que estos tenemos las rutas definidas, todavia no hemos añadido las rutas, estas rutas a la parte principal, que es taskapi