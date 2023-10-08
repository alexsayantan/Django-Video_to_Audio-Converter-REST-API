from .models import User, Media
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'create_at']

class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = ['id', 'media', 'user'] 
        extra_kwargs = {'user': {'read_only': True} }

    def create(self, validated_data):
        media = Media.objects.create(**validated_data, user=self.context['request'].user)
        return media

