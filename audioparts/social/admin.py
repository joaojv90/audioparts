from django.contrib import admin
from .models import Social

class SocialAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

# Register your models here.
admin.site.register(Social,SocialAdmin)