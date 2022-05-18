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
router.register(r"sensors", views.SensorViewSet, basename="sensors")

sensors_router = routers.NestedSimpleRouter(router, r"sensors", lookup="sensor")
sensors_router.register(r"logs", views.LogViewSet, basename="logs")

###
# URLs
###
urlpatterns = [
    re_path(
        r"^webhook/$",
        views.webhook,
        name="webhook",
    ),
    re_path(
        r"sensors/(?P<pk>\d+)/dashboard-data",
        views.DashboardDataAPIView.as_view(),
        name="dashboard-data",
    ),
    re_path(
        r"sensors/(?P<pk>\d+)/metrics",
        views.MetricsAPIView.as_view(),
        name="metrics",
    ),
    re_path(r"^", include(router.urls)),
    re_path(r"^", include(sensors_router.urls)),
]
