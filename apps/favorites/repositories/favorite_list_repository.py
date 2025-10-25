from apps.favorites.models.favorite_list_model import FavoriteList


class FavoriteListRepository:
    @staticmethod
    def create(user, name="Minha Lista de Favoritos"):
        return FavoriteList.objects.create(user=user, name=name)

    @staticmethod
    def get_all_by_user(user):
        return FavoriteList.objects.filter(user=user)

    @staticmethod
    def get_by_user_and_id(user, list_id):
        return FavoriteList.objects.filter(id=list_id, user=user).first()
    
    @staticmethod
    def update(user, list_id, name):
        favorite_list = FavoriteList.objects.filter(id=list_id, user=user).first()
        if favorite_list:
            favorite_list.name = name
            favorite_list.save()
        return favorite_list

    @staticmethod
    def get_by_share_uuid(share_uuid):
        return FavoriteList.objects.filter(share_uuid=share_uuid).first()

    @staticmethod
    def delete_by_user_and_id(user, list_id):
        FavoriteList.objects.filter(id=list_id, user=user).delete()

favorite_list_repository = FavoriteListRepository()
