import json

from django.http import HttpResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from rest_framework import status

import sensors.models as models


# Create your views here.
@csrf_exempt
@require_http_methods(["POST"])
def fucas_webhook(request):
    def get_sensor_instance(data):
        dev_eui = data['payload']['end_device_ids']['dev_eui']
        sensor, created = models.Sensor.objects.get_or_create(dev_eui=dev_eui)
        return sensor

    try:
        # Retrieve and clean data from request
        jsondata = request.body.decode('utf8')
        data = json.loads(jsondata)
        print({
            'service': 'sensor',
            'msg': 'WEBHOOK_RECEIVED',
            'device_id': data.get('device_id', None),
            'received_at': data.get('received_at', None),
            'payload': data
        })

        # Get sensor and register log
        sensor = get_sensor_instance(data=data)
        decoded_payload = data['payload']['uplink_message']['decoded_payload']
        log = models.Log.objects.create(
            sensor=sensor,
            timestamp=timezone.now(),
            **decoded_payload
        )

        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

    except BaseException as e:
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
