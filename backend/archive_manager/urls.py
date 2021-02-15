from django.urls import include, path
from rest_framework import routers

from .views import BuildingsList

urlpatterns = [path("buildings", BuildingsList.as_view(), name="buildings")]
