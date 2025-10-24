import pytest
from django.urls import reverse
from apps.favorites.models.favorite_model import Favorite
from misc.request_mixin import AuthRequestMixin



@pytest.mark.django_db
class TestFavoriteView(AuthRequestMixin):
    base_uri = "/api/favorites/"

    def test_add_favorite(self, api_client, superuser, favorite_user):
        response = self.auth_post(api_client, admin=superuser, body=favorite_user)
        
        assert response.status_code == 201
        assert Favorite.objects.count() == 1
        assert Favorite.objects.first().title == "Matrix"

    def test_list_favorites(self, api_client, superuser, favorite_user):
        Favorite.objects.create(user=superuser, **favorite_user)
        
        response = self.auth_get(api_client, admin=superuser)
        
        assert response.status_code == 200
        assert len(response.json()) == 1
        assert response.json()[0]["tmdb_id"] == 603

    def test_delete_favorite(self, api_client, superuser, favorite_user):
        favorite = Favorite.objects.create(user=superuser, **favorite_user)
        
        response = self.auth_delete(api_client, admin=superuser, obj=favorite)
        
        assert response.status_code == 204
        assert Favorite.objects.count() == 0