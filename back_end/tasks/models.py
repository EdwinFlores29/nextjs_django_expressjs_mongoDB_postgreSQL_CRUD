from django.db import models

# Create your models here.
class Task(models.Model): #aca hereda desde models la clase .Model
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True) #puede ser nulo o estar vacio
    done = models.BooleanField(default=False) #por defecto false
    created_at = models.DateTimeField(auto_now_add=True)  #aca para guardar la fecha de creacion, sino se añade que coloque la fecha actual
