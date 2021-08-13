import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from rest_framework import status


# Create your views here.
@csrf_exempt
@require_http_methods(["POST"])
def fucas_webhook(request):
    try:
        # Retrieve and clean data from request
        jsondata = request.body.decode('utf8').replace("'", '"').replace('\n', '')
        data = json.loads(jsondata)
        print({
            'service': 'sensor',
            'msg': 'WEBHOOK_RECEIVED',
            'payload': str(data),
        })
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
    except BaseException as e:
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
