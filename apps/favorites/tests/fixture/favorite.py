import pytest


@pytest.fixture()
def favorite_user():
    return {
            "tmdb_id": 603,
            "title": "Matrix",
            "poster_path": "/lDqMDI3xpbB9UQRyeXfei0MXhqb.jpg",
            "overview": "Thomas Anderson descobre a Matrix.",
            "release_date": "1999-03-31",
            "vote_average": 8.2,
            "vote_count": 27000,
            "genres": [{"id": 28, "name": "Ação"}],
        }

