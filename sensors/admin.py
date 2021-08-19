from django.contrib import admin

import sensors.models as models

# Register your models here.

@admin.register(models.Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_filter = ('name',)
    list_display = ('name', 'dev_eui')


@admin.register(models.Log)
class LogAdmin(admin.ModelAdmin):
    list_display = ('sensor', 'timestamp')