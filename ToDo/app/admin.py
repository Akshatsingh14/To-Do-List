from django.contrib import admin
from .models import List, History

# Register your models here.
@admin.register(List)
class NameAdmin(admin.ModelAdmin):
    list_display = ['task']

@admin.register(History)
class NameAdmin(admin.ModelAdmin):
    list_display = ['dtask']