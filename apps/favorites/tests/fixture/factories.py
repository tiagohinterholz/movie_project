import pytest
import uuid


@pytest.fixture
def favorite_list_factory(db, faker, user_factory):
    from apps.favorites.models.favorite_list_model import FavoriteList

    def make_favorite_list(
        *,
        user=None,
        name=None,
        count=1,
        **extra,
    ):
        favorite_lists = []

        if not user:
            user = user_factory()

        for _ in range(count):
            favorite_list = FavoriteList.objects.create(
                user=user,
                name=name or faker.sentence(nb_words=3),
                share_uuid=uuid.uuid4(),
                **extra,
            )
            favorite_lists.append(favorite_list)

        return favorite_lists if count > 1 else favorite_lists[0]

    return make_favorite_list


@pytest.fixture
def favorite_factory(db, faker, user_factory, favorite_list_factory):
    from apps.favorites.models.favorite_model import Favorite

    def make_favorite(
        *,
        favorite_list=None,
        count=1,
        **extra,
    ):
        favorites = []

        if not favorite_list:
            user = user_factory()
            favorite_list = favorite_list_factory(user=user)

        for _ in range(count):
            favorite = Favorite.objects.create(
                favorite_list=favorite_list,
                tmdb_id=extra.get("tmdb_id", faker.random_int(min=100, max=99999)),
                title=extra.get("title", faker.sentence(nb_words=3)),
                original_title=extra.get("original_title", faker.word()),
                overview=extra.get("overview", faker.text(max_nb_chars=150)),
                poster_path=extra.get("poster_path", f"/images/{uuid.uuid4()}.jpg"),
                backdrop_path=extra.get("backdrop_path", f"/backdrops/{uuid.uuid4()}.jpg"),
                release_date=extra.get("release_date", str(faker.date_this_century())),
                vote_average=extra.get("vote_average", faker.pyfloat(min_value=0, max_value=10)),
                vote_count=extra.get("vote_count", faker.random_int(min=10, max=5000)),
                genres=extra.get("genres", [{"id": 28, "name": "Ação"}]),
                runtime=extra.get("runtime", faker.random_int(min=60, max=180)),
                status=extra.get("status", faker.word()),
            )
            favorites.append(favorite)

        return favorites if count > 1 else favorites[0]

    return make_favorite