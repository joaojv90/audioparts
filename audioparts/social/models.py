from django.db import models

class Social(models.Model):
    key = models.SlugField(verbose_name= 'Clave', max_length = 100, unique = True)
    name = models.CharField(verbose_name='Red Social', max_length = 200)
    link = models.URLField(verbose_name='URL',max_length = 200, null= True, blank=True)
    created = models.DateTimeField(
        auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(
        auto_now=True, verbose_name='Fecha de Actualización')

    class Meta:
        verbose_name = 'Red Social'
        verbose_name_plural = 'Redes Sociales'
        ordering = ['name']

    def __str__(self):
        return self.name
