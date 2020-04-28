from django.contrib import admin
from .models import Baby

class StatusAdmin(admin.ModelAdmin):
    list_display = ['name','lastName','gender','parent']
admin.site.register(Baby,StatusAdmin)
