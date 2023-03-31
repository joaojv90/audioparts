from django.db import models

class Accessory (models.Model):
    name = models.CharField (max_length=150,verbose_name='Nombre')
    model = models.CharField (max_length=150,verbose_name='Modelo')    
    image = models.ImageField(verbose_name='Imagen', upload_to='Accesorios')
    created = models.DateTimeField(
        auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(
        auto_now=True, verbose_name='Fecha de Actualización')
    
    class Meta:
        verbose_name = 'Herramienta & Accesorio'
        verbose_name_plural = 'Herramientas & Accesorios'
        ordering = ['name']

    def __str__(self):
        return self.name
