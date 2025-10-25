from django.urls import reverse
from rest_framework.exceptions import ValidationError
from apps.favorites.repositories import favorite_list_repository
from apps.favorites.repositories.favorite_repository import favorite_repository


class FavoriteService:
    @staticmethod
    def add_favorite(user, favorite_list_id, data):
        favorite_list = favorite_list_repository.get_by_user_and_id(user, favorite_list_id)
        if not favorite_list:
            raise ValidationError("Lista de favoritos não encontrada.")

        existing = favorite_repository.get_by_user_and_tmdb(favorite_list, data.get("tmdb_id"))
        if existing:
            raise ValidationError("Este filme já está nos seus favoritos nesta lista.")

        return favorite_repository.create(favorite_list, data)

    @staticmethod
    def list_favorites(user, favorite_list_id):
        favorite_list = favorite_list_repository.get_by_user_and_id(user, favorite_list_id)
        if not favorite_list:
            raise ValidationError("Lista de favoritos não encontrada.")

        return favorite_repository.get_all_by_list(favorite_list)

    @staticmethod
    def remove_favorite(user, favorite_list_id, favorite_id):
        favorite_list = favorite_list_repository.get_by_user_and_id(user, favorite_list_id)
        if not favorite_list:
            raise ValidationError("Lista de favoritos não encontrada.")

        existing = favorite_repository.get_by_user_and_id(favorite_list, favorite_id)
        if not existing:
            raise ValidationError("Filme não encontrado nesta lista.")

        favorite_repository.delete(favorite_list, favorite_id)
        return None

    @staticmethod
    def get_share_link(favorite_list_id, request):
        favorite_list = favorite_list_repository.get_by_id(favorite_list_id)
        if not favorite_list or not favorite_list.favorites.exists():
            raise ValidationError("Lista inválida ou sem favoritos para compartilhar.")

        link = request.build_absolute_uri(
            reverse("favorite-share", kwargs={"share_uuid": favorite_list.share_uuid})
        )
        return {"share_link": link}


favorite_service = FavoriteService()
