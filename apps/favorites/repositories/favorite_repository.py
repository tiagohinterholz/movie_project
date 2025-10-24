from apps.favorites.models.favorite_model import Favorite


class FavoriteRepository:
    @staticmethod
    def create(user, data):
        return Favorite.objects.create(user=user, **data)

    @staticmethod
    def get_all_by_user(user):
        return Favorite.objects.filter(user=user)

    @staticmethod
    def get_by_user_and_tmdb(user, tmdb_id):
        return Favorite.objects.filter(user=user, tmdb_id=tmdb_id).first()
    
    @staticmethod
    def get_by_user_and_id(user, favorite_id):
        return Favorite.objects.filter(id=favorite_id, user=user).first()

    @staticmethod
    def delete(user, favorite_id):
        Favorite.objects.filter(user=user, id=favorite_id).delete()
