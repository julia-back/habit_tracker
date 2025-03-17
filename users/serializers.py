from .models import User
from rest_framework.serializers import ModelSerializer


class UserRegisterSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "username", "password"]
    
    def create(self, validated_data):
        model = self.Meta.model
        instance = model.objects.create_user(**validated_data)
        return instance
