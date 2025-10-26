from django.urls import path
from apps.favorites.views.favorite_view import (
    FavoriteCreateView,
    FavoriteDeleteView,
)

urlpatterns = [
    path("", FavoriteCreateView.as_view(), name="favorite-list-create"),
    path("<uuid:favorite_id>/", FavoriteDeleteView.as_view(), name="favorite-delete"),
]
