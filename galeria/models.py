from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Usuario(AbstractUser):
    imagen = models.ImageField(upload_to='foto_perfil')
    edad= models.PositiveIntegerField(blank=True,null=True)

    def __str__(self):
        return self.username

class Galeria(models.Model):
    usuario= models.ManyToManyField(Usuario)

    nombre= models.CharField(max_length=120)
    descripcion= models.TextField()

    def __str__(self):
        return self.nombre


class Foto(models.Model):
    usuario= models.ForeignKey(Usuario,on_delete=models.CASCADE,blank=True,null=True)
    galeria= models.ForeignKey(Galeria,on_delete=models.CASCADE,blank=True,null=True)

    imagen = models.ImageField(upload_to='fotos')
    fecha= models.DateField()
    descripcion= models.TextField()

    def __str__(self):
        return self.id
