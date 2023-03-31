from django.db import models

class Backlight (models.Model):
    code = models.CharField (max_length=150,verbose_name='Código')
    trademark = models.CharField (max_length=150,verbose_name='Marca')
    model = models.CharField (max_length=150,verbose_name='Modelo')
    leds = models.CharField (max_length=10,verbose_name='LEDS')
    voltage = models.CharField (max_length=10,verbose_name='Voltaje')
    piece = models.CharField (max_length=50,verbose_name='Piezas')
    references = models.CharField (max_length=150,verbose_name='Refencia',null= True, blank=True)
    image = models.ImageField(verbose_name='Imagen', upload_to='Backlights')
    created = models.DateTimeField(
        auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(
        auto_now=True, verbose_name='Fecha de Actualización')
    
    class Meta:
        verbose_name = 'Backlight / Tira LED'
        verbose_name_plural = 'Backlights / Tira LEDs'
        ordering = ['code']

    def __str__(self):
        return self.code
