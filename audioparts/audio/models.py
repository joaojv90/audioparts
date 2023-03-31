from django.db import models

class Audio (models.Model):
    code = models.CharField (max_length=150,verbose_name='Código')
    description = models.CharField (max_length=150,verbose_name='Descripción')    
    image = models.ImageField(verbose_name='Imagen', upload_to='Audio')
    created = models.DateTimeField(
        auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(
        auto_now=True, verbose_name='Fecha de Actualización')
    
    class Meta:
        verbose_name = 'Audio'
        verbose_name_plural = 'Audio'
        ordering = ['code']

    def __str__(self):
        return self.code
