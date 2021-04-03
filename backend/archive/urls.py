from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path(r"silk/", include("silk.urls", namespace="silk")),
    path("api/", include("backend.archive_manager.urls")),
    path("", include("frontend.urls")),

]
