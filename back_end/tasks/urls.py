from rest_framework import routers
from .api import TaskViewSet

router = routers.DefaultRouter() #aca hace el llamado a una funcion

router.register('api/tasks', TaskViewSet, 'tasks') #aqui vamos a colocar como se va llamar todas las rutas

urlpatterns = router.urls #aca practicamente es un arreglo donde a va tener todos los valores, linea 6
# de esta forma tenemos urls, ahora añadir en la aplicacion principal dentro del archivo urls.py de la carpeta tastapi