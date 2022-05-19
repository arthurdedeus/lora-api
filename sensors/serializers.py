from datetime import timedelta

from rest_framework import serializers
from rest_framework.fields import empty

from sensors import helpers
from sensors.models import Sensor, Log


class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = ("id", "timestamp", "pressure", "temperature", "humidity")


class SensorLogSerializer(serializers.ModelSerializer):
    logs = LogSerializer(many=True)

    class Meta:
        model = Sensor
        fields = ("id", "name", "logs")


class SensorSerializer(serializers.ModelSerializer):
    metrics = serializers.SerializerMethodField()
    logs = LogSerializer(many=True)

    class Meta:
        model = Sensor
        fields = "__all__"

    def get_metrics(self, instance):
        return helpers.get_metrics(instance.logs.all())


class DashboardDataSerializer(serializers.ModelSerializer):
    temperature = serializers.SerializerMethodField()
    pressure = serializers.SerializerMethodField()
    humidity = serializers.SerializerMethodField()

    class Meta:
        model = Sensor
        fields = ("temperature", "pressure", "humidity")

    def get_temperature(self, instance):
        timestamp = instance.logs.last().timestamp - timedelta(hours=3)
        return {
            "id": 1,
            "type": "temperature",
            "title": "Temperatura",
            "measure": f"{instance.logs.last().temperature}°C",
            "date": timestamp.strftime("%d/%m/%Y"),
            "time": timestamp.strftime("%H:%M"),
            "icon": "thermometer",
        }

    def get_humidity(self, instance):
        timestamp = instance.logs.last().timestamp - timedelta(hours=3)
        return {
            "id": 2,
            "type": "humidity",
            "title": "Umidade",
            "measure": f"{instance.logs.last().humidity}%",
            "date": timestamp.strftime("%d/%m/%Y"),
            "time": timestamp.strftime("%H:%M"),
            "icon": "droplet",
        }

    def get_pressure(self, instance):
        timestamp = instance.logs.last().timestamp - timedelta(hours=3)
        return {
            "id": 3,
            "type": "pressure",
            "title": "Pressão",
            "measure": f"{instance.logs.last().pressure}hPa",
            "date": timestamp.strftime("%d/%m/%Y"),
            "time": timestamp.strftime("%H:%M"),
            "icon": "arrow-down",
        }


class MetricsSerializer(serializers.ModelSerializer):
    temperature = serializers.SerializerMethodField()
    pressure = serializers.SerializerMethodField()
    humidity = serializers.SerializerMethodField()

    def __init__(self, instance=None, data=empty, **kwargs):
        super().__init__(instance, data, **kwargs)
        self.metrics = helpers.get_metrics(instance.logs.all())

    class Meta:
        model = Sensor
        fields = ("temperature", "pressure", "humidity")

    def get_temperature(self, instance):
        return self.metrics.get("temperature")

    def get_humidity(self, instance):
        return self.metrics.get("humidity")

    def get_pressure(self, instance):
        return self.metrics.get("pressure")
