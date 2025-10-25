from apps.favorites.models.favorite_model import Favorite


class FavoriteRepository:
    @staticmethod
    def create(favorite_list, data):
        return Favorite.objects.create(favorite_list=favorite_list, **data)

    @staticmethod
    def get_all_by_user(user):
        return Favorite.objects.filter(favorite_list__user=user)

    @staticmethod
    def get_by_user_and_tmdb(favorite_list, tmdb_id):
        return Favorite.objects.filter(favorite_list=favorite_list, tmdb_id=tmdb_id).first()
    
    @staticmethod
    def get_by_user_and_id(favorite_list, favorite_id):
        return Favorite.objects.filter(id=favorite_id, favorite_list=favorite_list).first()

    @staticmethod
    def delete(favorite_list, favorite_id):
        Favorite.objects.filter(favorite_list=favorite_list, id=favorite_id).delete()

favorite_repository = FavoriteRepository()