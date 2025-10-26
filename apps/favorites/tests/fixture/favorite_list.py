import pytest


@pytest.fixture
def favorite_list_dict(user_factory):
    user = user_factory()
    return {
        "user": user.id,
        "name": "Lista do Tiago",
    }
    
    
@pytest.fixture
def favorite_list_object(db, user_factory):
    from apps.favorites.models.favorite_list_model import FavoriteList
    user = user_factory()
    favorite_list = FavoriteList.objects.create(
        user=user,
        name="Minha Lista de Teste",
    )
    return favorite_list