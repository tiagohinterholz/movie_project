from apps.favorites.models.favorite_model import Favorite
from rest_framework.serializers import ModelSerializer


class FavoriteSerializer(ModelSerializer):
    class Meta:
        model = Favorite
        fields = "__all__"