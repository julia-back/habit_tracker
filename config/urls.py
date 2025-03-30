from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("habit_tracker/", include("habit_tracker.urls", namespace="habit_tracker")),
    path("users/", include("users.urls", namespace="users")),

    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger_docs"),
    path("api/docs/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc_docs"),
]
