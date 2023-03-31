from django.contrib import admin
from .models import Backlight

class BacklightAdmin (admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Backlight, BacklightAdmin)
