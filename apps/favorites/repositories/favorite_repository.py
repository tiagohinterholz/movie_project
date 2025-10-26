from apps.favorites.models.favorite_model import Favorite


class FavoriteRepository:
    @staticmethod
    def create(data):
        return Favorite.objects.create(**data)

    @staticmethod
    def get_all_by_user(user):
        return Favorite.objects.filter(favorite_list__user=user)
    
    @staticmethod
    def get_all_by_list(favorite_list):
        return Favorite.objects.filter(favorite_list=favorite_list)

    @staticmethod
    def get_by_user_and_tmdb(favorite_list, tmdb_id):
        return Favorite.objects.filter(favorite_list=favorite_list, tmdb_id=tmdb_id).first()
    
    @staticmethod
    def get_by_user_and_id(favorite_list, favorite_id):
        return Favorite.objects.filter(id=favorite_id, favorite_list=favorite_list).first()

    @staticmethod
    def delete(favorite):
        favorite.delete()

favorite_repository = FavoriteRepository()