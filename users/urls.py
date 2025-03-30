from django.urls import path

from . import views
from .apps import UsersConfig

app_name = UsersConfig.name

urlpatterns = [
    path("token/", views.CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token_refresh/", views.CustomTokenRefreshView.as_view(), name="token_refresh"),

    path("user_register/", views.UserRegisterAPIView.as_view(), name="user_register"),
    path("user_profile/<int:pk>/", views.UserRetrieveAPIView.as_view(), name="user_retrieve"),
    path("user_profile/update/<int:pk>/", views.UserUpdateAPIView.as_view(), name="user_update"),
    path("user_profile/delete/<int:pk>/", views.UserDestroyAPIView.as_view(), name="user_delete"),
]
