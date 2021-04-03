from .views import MainPageView
from django.urls import path

urlpatterns = [# rest of urls
              path(r'', MainPageView.as_view(),name='app')]