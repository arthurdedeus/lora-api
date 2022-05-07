from django.contrib import admin

import sensors.models as models


# Register your models here.

@admin.register(models.Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_filter = ('name',)
    list_display = ('name', 'dev_eui', 'id')


@admin.register(models.Log)
class LogAdmin(admin.ModelAdmin):
    list_display = ('sensor', 'timestamp')


@admin.register(models.Warning)
class WarningAdmin(admin.ModelAdmin):
    list_display = ('sensor', 'measurement', 'timestamp')


@admin.register(models.WarningThreshold)
class WarningAdmin(admin.ModelAdmin):
    list_display = ('sensor',)
