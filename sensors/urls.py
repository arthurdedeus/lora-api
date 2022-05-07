"""
API V1: Sensors Urls
"""
###
# Libraries
###
from django.urls import re_path, include
from rest_framework_nested import routers

import sensors.views as views


###
# Routers
###
""" Main router """
router = routers.SimpleRouter()
router.register(r'sensors', views.SensorViewSet, basename='sensors')

###
# URLs
###
urlpatterns = [
    re_path(
        r'^fucas-webhook/$',
        views.fucas_webhook,
        name='fucas_webhook',
    ),
    re_path(r'^', include(router.urls)),
]
