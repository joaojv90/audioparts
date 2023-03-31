from django.contrib import admin
from .models import Accessory

class AccessoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Accessory, AccessoryAdmin)