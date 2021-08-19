from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Sensor(models.Model):
    name = models.CharField(
        max_length=128,
        null=True,
        blank=True,
        help_text=_('Name of the sensor')
    )
    app_eui = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        help_text=_('App EUI')
    )
    dev_eui = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        help_text=_('Device EUI')
    )

    def __str__(self):
        return str(self.name)


class Log(models.Model):
    # Relations
    sensor = models.ForeignKey(
        'sensors.Sensor',
        on_delete=models.SET_NULL,
        null=True,
    )
    # Log data
    timestamp = models.DateTimeField(
        null=True,
        blank=True,
        help_text=_('Time when the log was received')
    )
    pressure = models.FloatField(
        null=True,
        blank=True,
        help_text=_('Atmospheric pressure')
    )
    temperature = models.FloatField(
        null=True,
        blank=True,
        help_text=_('Ambient temperature')
    )
    humidity = models.FloatField(
        null=True,
        blank=True,
        help_text=_('Ambient humidity')
    )
    accel_x_axis = models.FloatField(
        null=True,
        blank=True,
        help_text=_('Acceleration in x axis')
    )
    accel_y_axis = models.FloatField(
        null=True,
        blank=True,
        help_text=_('Acceleration in y axis')
    )
    accel_z_axis = models.FloatField(
        null=True,
        blank=True,
        help_text=_('Acceleration in z axis')
    )
    gyro_x_axis = models.FloatField(
        null=True,
        blank=True,
        help_text=_('Gyroscope in x axis')
    )
    gyro_y_axis = models.FloatField(
        null=True,
        blank=True,
        help_text=_('Gyroscope in y axis')
    )
    gyro_z_axis = models.FloatField(
        null=True,
        blank=True,
        help_text=_('Gyroscope in z axis')
    )
    magnometer = models.FloatField(
        null=True,
        blank=True,
        help_text=_('Magnometer')
    )
    bat_voltage = models.FloatField(
        null=True,
        blank=True,
        help_text=_('Battery voltage')
    )

    def __str__(self):
        return self.timestamp.strftime('%d/%m/%Y - %H:%M')
