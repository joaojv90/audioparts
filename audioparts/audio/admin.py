from django.contrib import admin
from .models import Audio

class AudioAdmin (admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Audio, AudioAdmin)