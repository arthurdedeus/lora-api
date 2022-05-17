from rest_framework import serializers

from sensors import helpers
from sensors.models import Sensor, Log


class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = ('id', 'timestamp', 'pressure', 'temperature', 'humidity')


class SensorLogSerializer(serializers.ModelSerializer):
    logs = LogSerializer(many=True)

    class Meta:
        model = Sensor
        fields = ('id', 'name', 'logs')


class SensorSerializer(serializers.ModelSerializer):
    metrics = serializers.SerializerMethodField()
    logs = LogSerializer(many=True)

    class Meta:
        model = Sensor
        fields = '__all__'

    def get_metrics(self, instance):
        return helpers.get_metrics(instance.logs.all())
