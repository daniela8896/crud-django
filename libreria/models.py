from django.db import models

# Create your models here.

class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    imagen = models.ImageField(upload_to='imagenes/', null=True, verbose_name='Imagen')
    descripcion = models.TextField(verbose_name='Descripción', null=True)

    #con esta instruccion edito como se ven la descripcion en el admin
    def __str__(self):
        fila = "Titulo:" + self.titulo + " | " + "Descripción:" + self.descripcion
        return fila
    #con esta instruccion al borrar una imagen del admin se borra de la carpeta imagenes del visual
    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()    
