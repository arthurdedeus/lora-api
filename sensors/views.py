import datetime
import json

from django.db.models import Prefetch
from django.http import HttpResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

import sensors.models as models
from sensors.serializers import (
    DashboardDataSerializer,
    LogSerializer,
    MetricsSerializer,
    SensorSerializer,
)


# Create your views here.
@csrf_exempt
@require_http_methods(["POST"])
def webhook(request):
    def get_sensor_instance(data):
        dev_eui = data["end_device_ids"]["dev_eui"]
        sensor, created = models.Sensor.objects.get_or_create(dev_eui=dev_eui)
        return sensor

    try:
        # Retrieve and clean data from request
        jsondata = request.body.decode("utf8")
        data = json.loads(jsondata)
        if data.get("simulated", None):
            return HttpResponse(status=status.HTTP_418_IM_A_TEAPOT)
        print(
            {
                "service": "sensor",
                "msg": "WEBHOOK_RECEIVED",
                "device_id": data.get("device_id", None),
                "received_at": data.get("received_at", None),
                "payload": data,
            }
        )

        # Get sensor and register log
        sensor = get_sensor_instance(data=data)
        decoded_payload = data["uplink_message"]["decoded_payload"]
        models.Log.objects.create(
            sensor=sensor, timestamp=timezone.now(), **decoded_payload
        )

        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

    except BaseException as e:
        print(
            {
                "service": "sensor",
                "msg": "WEBHOOK_ERROR",
                "error": str(e),
            }
        )
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)


class SensorViewSet(ModelViewSet):
    serializer_class = SensorSerializer
    permission_classes = [
        IsAuthenticated,
    ]

    def get_queryset(self):
        last_90_days = timezone.now() - datetime.timedelta(days=90)
        logs = models.Log.objects.filter(timestamp__gte=last_90_days)
        return models.Sensor.objects.all().prefetch_related(
            Prefetch("logs", queryset=logs)
        )

    def retrieve(self, request, *args, **kwargs):
        ret = super().retrieve(request, *args, **kwargs)
        return ret


class LogViewSet(RetrieveAPIView):
    serializer_class = LogSerializer
    permission_classes = [
        IsAuthenticated,
    ]
    pagination_class = None

    def get_queryset(self):
        return models.Log.objects.filter(sensor_id=self.kwargs.get("pk")).order_by(
            "-id"
        )[:30]

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class DashboardDataAPIView(RetrieveAPIView):
    serializer_class = DashboardDataSerializer
    permission_classes = [
        IsAuthenticated,
    ]
    queryset = models.Sensor.objects.all()
    pagination_class = None

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class MetricsAPIView(RetrieveAPIView):
    serializer_class = MetricsSerializer
    permission_classes = [
        IsAuthenticated,
    ]
    queryset = models.Sensor.objects.all()
    pagination_class = None

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
