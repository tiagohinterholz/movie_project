import pytest
from apps.favorites.models.favorite_list_model import FavoriteList
from misc.request_mixin import AuthRequestMixin


@pytest.mark.django_db
class TestFavoriteListView(AuthRequestMixin):
    base_uri = "/api/favorite-lists/"

    def test_create_favorite_list(self, api_client, user_factory, favorite_list_dict):
        user = user_factory()
        
        response = self.auth_post(
            api_client, 
            admin=user, 
            body=favorite_list_dict
        )

        assert response.status_code == 201
        assert FavoriteList.objects.count() == 1

        favorite_list = FavoriteList.objects.first()
        assert favorite_list.name == "Lista do Tiago"

    def test_create_favorite_list_with_no_name(self, api_client, user_factory):
        user = user_factory()
        response = self.auth_post(api_client, admin=user, body={})

        assert response.status_code == 400
        response_data = response.json()

        assert "name" in response_data or "obrigatório" in str(response_data).lower()
    
    def test_list_all_favorite_lists(self, api_client, user_factory, favorite_list_factory):
        user = user_factory()
        favorite_list_factory(user=user, count=3)

        response = self.auth_get(api_client, admin=user)

        assert response.status_code == 200
        data = response.json()

        assert isinstance(data, list)
        assert len(data) == 3

        db_names = list(FavoriteList.objects.filter(user=user).values_list("name", flat=True))
        response_names = [item["name"] for item in data]

        assert sorted(db_names) == sorted(response_names)
    
    def test_update_favorite_list_name(self, api_client, favorite_list_object):
        user = favorite_list_object.user
        new_name = "Lista Atualizada"
        body = {"name": new_name}

        response = self.auth_patch(
            api_client, 
            admin=user, 
            obj=favorite_list_object, 
            body=body
        )

        assert response.status_code == 200

        favorite_list_object.refresh_from_db()
        assert favorite_list_object.name == new_name

        data = response.json()
        assert data["name"] == new_name
    
    def test_delete_favorite_list(self, api_client, favorite_list_object):
        user = favorite_list_object.user

        response = self.auth_delete(api_client, admin=user, obj=favorite_list_object)

        assert response.status_code == 204
        assert not FavoriteList.objects.filter(id=favorite_list_object.id).exists()


@pytest.mark.django_db
class TestFavoriteListShareView(AuthRequestMixin):
    base_uri_template = "/api/favorite-lists/share/{list_id}/generate/"

    def test_generate_share_link(self, api_client, favorite_list_object, favorite_factory):
        user = favorite_list_object.user
        favorite_factory(favorite_list=favorite_list_object, count=2)

        uri = self.base_uri_template.format(list_id=favorite_list_object.id)
        response = self.auth_post(api_client, admin=user, uri=uri)

        assert response.status_code == 200
        data = response.json()
        assert "share_link" in data
        assert str(favorite_list_object.share_uuid) in data["share_link"]
    

@pytest.mark.django_db
class TestFavoriteListGetPublicView(AuthRequestMixin):
    base_uri_template = "/api/favorite-lists/share/{share_uuid}/"

    def test_access_shared_favorite_list(self, api_client, favorite_list_object, favorite_factory):
        favorite_factory(favorite_list=favorite_list_object, count=3)
        share_uuid = favorite_list_object.share_uuid

        uri = self.base_uri_template.format(share_uuid=share_uuid)
        response = api_client.get(uri)

        assert response.status_code == 200
        data = response.json()
        assert len(data) == 3
        assert all("tmdb_id" in fav for fav in data)