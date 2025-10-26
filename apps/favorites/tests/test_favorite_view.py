import pytest
from apps.favorites.models.favorite_model import Favorite
from misc.request_mixin import AuthRequestMixin



@pytest.mark.django_db
class TestFavoriteView(AuthRequestMixin):
    base_uri_template = "/api/favorite-lists/{favorite_list_id}/favorites/"

    def test_create_favorite(
        self, api_client, favorite_dict, favorite_list_object
    ):
        base_uri = self.base_uri_template.format(favorite_list_id=favorite_list_object.id)
        response = self.auth_post(
            api_client, 
            admin=favorite_list_object.user, 
            body=favorite_dict,
            uri=base_uri
        )

        assert response.status_code == 201
        assert Favorite.objects.count() == 1

        favorite = Favorite.objects.first()
        assert favorite.title == "Matrix"
        assert favorite.favorite_list == favorite_list_object
        assert favorite.tmdb_id == favorite_dict["tmdb_id"]
    
    def test_list_favorites(self, api_client, favorite_list_object, favorite_factory):
        user = favorite_list_object.user
        favorite_factory(favorite_list=favorite_list_object, count=2)
        base_uri = self.base_uri_template.format(favorite_list_id=favorite_list_object.id)
        
        response = self.auth_get(api_client, admin=user, uri=base_uri)

        assert response.status_code == 200
        data = response.json()
        assert len(data) == 2

        tmdb_ids = [item["tmdb_id"] for item in data]
        db_tmdb_ids = list(Favorite.objects.values_list("tmdb_id", flat=True))

        assert sorted(tmdb_ids) == sorted(db_tmdb_ids)
    
    def test_delete_favorite(self, api_client, favorite_list_object, favorite_factory):
        user = favorite_list_object.user
        favorite = favorite_factory(favorite_list=favorite_list_object)

        base_uri = self.base_uri_template.format(favorite_list_id=favorite_list_object.id) + f'{favorite.id}/'

        response = self.auth_delete(api_client, admin=user, obj=favorite, uri=base_uri)

        assert response.status_code == 204
        assert Favorite.objects.count() == 0