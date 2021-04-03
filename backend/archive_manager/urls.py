from django.urls import path

from .views import BuildingsList

urlpatterns = [path("buildings", BuildingsList.as_view(), name="buildings")]
