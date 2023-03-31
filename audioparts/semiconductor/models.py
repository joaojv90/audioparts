from django.db import models

class Semiconductor (models.Model):
    code = models.CharField (max_length=50,verbose_name='Código')
    sort = models.CharField (max_length=50,verbose_name='Tipo')
    model = models.CharField (max_length=50,verbose_name='Modelo')
    description = models.CharField (max_length=150,verbose_name='Descripción')
    origin = models.CharField (max_length=50,verbose_name='Procedencia')
    image = models.ImageField(verbose_name='Imagen', upload_to='Semiconductores')
    created = models.DateTimeField(
        auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(
        auto_now=True, verbose_name='Fecha de Actualización')
    
    class Meta:
        verbose_name = 'Semiconductor'
        verbose_name_plural = 'Semiconductores'
        ordering = ['code']

    def __str__(self):
        return self.code
