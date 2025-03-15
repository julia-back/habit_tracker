from django.urls import path, include
from . import views
from .apps import UsersConfig


app_name = UsersConfig.name

urlpatterns = [
    path("token/", views.CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token_refresh/", views.CustomTokenRefreshView.as_view(), name="token_refresh"),
]
