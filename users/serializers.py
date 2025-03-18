from .models import User
from rest_framework import serializers
from config.settings import TELEGRAM_BOT_NAME


class UserRegisterSerializer(serializers.ModelSerializer):

    message = serializers.CharField(default=f"Добро пожаловать! Чтобы получать уведомления о "
                                            f"выполнении привычек, напишите нашему боту '/start'! "
                                            f"Ссылка на бота: {TELEGRAM_BOT_NAME}",
                                    read_only=True)

    class Meta:
        model = User
        fields = ["email", "username", "password", "message"]
    
    def create(self, validated_data):
        model = self.Meta.model
        instance = model.objects.create_user(**validated_data)
        return instance


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "username", "first_name", "last_name"]
