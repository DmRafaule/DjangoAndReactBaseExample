from django.contrib import admin
from .models import  AppModel

class AppModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

admin.site.register(AppModel, AppModelAdmin)
