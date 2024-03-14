from django.contrib.auth.models import User
from rest_framework import serializers
from advertisements.models import Advertisement, AdvertisementFavorites


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name',)


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""

    creator = UserSerializer(
        read_only=True,
    )

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'creator',
                  'status', 'created_at', 'updated_at', 'draft')

    def create(self, validated_data):
        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)

    def validate(self, data):
        user = self.context["request"].user
        if data.get('status') == 'CLOSED':
            return data
        if len(Advertisement.objects.filter(creator=user, status='OPEN')) >= 10:
            raise serializers.ValidationError("You can't open more than 10 ads")
        return data

class AdvertisementFavoritesSerializer(serializers.ModelSerializer):
    """Serializer для избранных объявлений."""
    advertisement = AdvertisementSerializer()

    class Meta:
        model = AdvertisementFavorites
        fields = ('user', 'advertisement')
