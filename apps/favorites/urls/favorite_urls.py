from django.urls import path
from apps.favorites.views.favorite_view import (
    FavoriteListCreateView,
    FavoriteDeleteView,
    FavoriteShareGenerateView,
    FavoriteShareView,
)

urlpatterns = [
    path("", FavoriteListCreateView.as_view(), name="favorite-list-create"),
    path("<uuid:pk>/", FavoriteDeleteView.as_view(), name="favorite-delete"),
    path("share/<uuid:share_uuid>/", FavoriteShareView.as_view(), name="favorite-share"),
    path("share/generate/", FavoriteShareGenerateView.as_view(), name="favorite-share-generate"),
]
