from django.contrib import admin
from .models import Miscellany

class MiscellanyAdmin (admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Miscellany, MiscellanyAdmin)

