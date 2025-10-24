from rest_framework.exceptions import ValidationError
from apps.favorites.repositories.favorite_repository import FavoriteRepository


class FavoriteService:
    @staticmethod
    def add_favorite(user, data):
        existing = FavoriteRepository.get_by_user_and_tmdb(user, data.get("tmdb_id"))
        if existing:
            raise ValidationError("Este filme já está nos seus favoritos.")

        return FavoriteRepository.create(user, data)

    @staticmethod
    def list_favorites(user):
        return FavoriteRepository.get_all_by_user(user)

    @staticmethod
    def remove_favorite(user, favorite_id):
        existing = FavoriteRepository.get_by_user_and_id(user, favorite_id)
        if not existing:
            raise ValidationError("Filme não encontrado nos seus favoritos.")

        FavoriteRepository.delete(user, favorite_id)
        return None

favorite_service = FavoriteService()