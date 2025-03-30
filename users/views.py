from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from .models import User
from .permissions import IsOwnerProfile
from .serializers import UserRegisterSerializer, UserSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    """Класс представления для получения токенов авторизации. Доступен неавторизованным пользователям."""

    permission_classes = [AllowAny]


class CustomTokenRefreshView(TokenRefreshView):
    """Класс представления для обновления токенов. Доступен неавторизованным пользователям."""

    permission_classes = [AllowAny]


class UserRegisterAPIView(generics.CreateAPIView):
    """
    Класс представлния для регистрации пользователя. В ответе возвращает
    ссылку на телеграмм бота и инструкцию для взаимодействия с ботом в поле message.
    Доступен неавторизованным пользователям.
    """

    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]


class UserRetrieveAPIView(generics.RetrieveAPIView):
    """
    Класс предствления для вывода конктретного объекта модели пользователя.
    Доступен пользователю, запрашивающему свой объект модели пользователя.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsOwnerProfile]


class UserUpdateAPIView(generics.UpdateAPIView):
    """
    Класс предствления для обновления объекта модели пользователя.
    Доступен пользователю, запрашивающему свой объект модели пользователя.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsOwnerProfile]


class UserDestroyAPIView(generics.DestroyAPIView):
    """
    Класс предствления для удаления объекта модели пользователя.
    Доступен пользователю, запрашивающему свой объект модели пользователя.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsOwnerProfile]
