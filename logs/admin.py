from django.contrib import admin

from django.contrib import admin
from .models import BodyLog

@admin.register(BodyLog)
class BodyLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'height', 'weight')