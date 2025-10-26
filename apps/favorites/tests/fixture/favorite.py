import pytest


@pytest.fixture
def favorite_dict(favorite_list_object):
    return {
        "favorite_list": str(favorite_list_object.id),
        "tmdb_id": 603,
        "title": "Matrix",
        "original_title": "The Matrix",
        "overview": "Thomas Anderson descobre a Matrix.",
        "poster_path": "/lDqMDI3xpbB9UQRyeXfei0MXhqb.jpg",
        "backdrop_path": "/matrix-bg.jpg",
        "release_date": "1999-03-31",
        "vote_average": 8.2,
        "vote_count": 27000,
        "genres": [{"id": 28, "name": "Ação"}],
        "runtime": 136,
        "status": "Released",
    }


@pytest.fixture
def favorite_object(db, favorite_list_object):
    from apps.favorites.models.favorite_model import Favorite
    favorite = Favorite.objects.create(
        favorite_list=favorite_list_object,
        tmdb_id=603,
        title="Matrix",
        original_title="The Matrix",
        overview="Thomas Anderson descobre a Matrix.",
        poster_path="/lDqMDI3xpbB9UQRyeXfei0MXhqb.jpg",
        backdrop_path="/matrix-bg.jpg",
        release_date="1999-03-31",
        vote_average=8.2,
        vote_count=27000,
        genres=[{"id": 28, "name": "Ação"}],
        runtime=136,
        status="Released",
    )
    return favorite