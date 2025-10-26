from django.urls import include, path
from apps.favorites.views.favorite_list_view import (
    FavoriteListView,
    FavoriteListDetailView,
)
from apps.favorites.views.favorite_share_view import (
    FavoriteShareGenerateView,
    FavoriteShareView,
)


urlpatterns = [
    path("", FavoriteListView.as_view(), name="favorite-list"),
    path("<uuid:favorite_list_id>/", FavoriteListDetailView.as_view(), name="favorite-list-detail"),
    path("<uuid:favorite_list_id>/favorites/", include("apps.favorites.urls.favorite_urls")),
    
    path("share/<uuid:share_uuid>/", FavoriteShareView.as_view(), name="favorite-share"),
    path("share/<uuid:favorite_list_id>/generate/", FavoriteShareGenerateView.as_view(), name="favorite-share-generate"),
]