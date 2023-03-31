from django.contrib import admin
from .models import Semiconductor

class SemiconductorAdmin (admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Semiconductor,SemiconductorAdmin)