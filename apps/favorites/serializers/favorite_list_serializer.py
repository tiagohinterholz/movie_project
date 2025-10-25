from rest_framework import serializers
from apps.favorites.models.favorite_list_model import FavoriteList
from apps.favorites.serializers.favorite_serializer import FavoriteSerializer


class FavoriteListSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteList
        fields = [
            "id",
            "name",
            "share_uuid",
            "created_at",
        ]
        read_only_fields = ["id", "share_uuid", "created_at"]


class FavoriteListDetailSerializer(serializers.ModelSerializer):
    favorites = FavoriteSerializer(many=True, read_only=True)

    class Meta:
        model = FavoriteList
        fields = [
            "id",
            "name",
            "share_uuid",
            "created_at",
            "favorites",
        ]
        read_only_fields = ["id", "share_uuid", "created_at", "favorites"]
