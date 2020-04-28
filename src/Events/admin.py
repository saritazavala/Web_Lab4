from django.contrib import admin
from .models import Event

class StatusAdmin(admin.ModelAdmin):
    list_display = ['description','type','date','baby']
admin.site.register(Event,StatusAdmin)
