from rest_framework.exceptions import ValidationError
from apps.favorites.repositories.favorite_list_repository import favorite_list_repository


class FavoriteListService:
    @staticmethod
    def create(user, name: str):
        if not name:
            raise ValidationError("O campo 'name' é obrigatório.")
        return favorite_list_repository.create(user, name)

    @staticmethod
    def all_lists_by_user(user):
        return favorite_list_repository.get_all_by_user(user)

    @staticmethod
    def list_by_user(user, favorite_list_id):
        favorite_list = favorite_list_repository.get_by_user_and_id(user, favorite_list_id)
        if not favorite_list:
            raise ValidationError("Lista não encontrada.")
        return favorite_list

    @staticmethod
    def update(user, favorite_list_id, name: str):
        if not name:
            raise ValidationError("O campo 'name' é obrigatório.")

        favorite_list = favorite_list_repository.get_by_user_and_id(user, favorite_list_id)
        if not favorite_list:
            raise ValidationError("Lista não encontrada.")

        updated_list = favorite_list_repository.update(user, favorite_list_id, name)
        if not updated_list:
            raise ValidationError("Erro ao atualizar a lista.")
        return updated_list

    @staticmethod
    def delete(user, favorite_list_id):
        favorite_list = favorite_list_repository.get_by_user_and_id(user, favorite_list_id)
        if not favorite_list:
            raise ValidationError("Lista não encontrada.")
        favorite_list_repository.delete_by_user_and_id(user, favorite_list_id)


favorite_list_service = FavoriteListService()
