from django.contrib import admin
from django.urls import path, include
from tasks.views import health

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("tasks.urls")),
    path("health/", health),
]