from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("habit_tracker/", include("habit_tracker.urls", namespace="habit_tracker")),
]
