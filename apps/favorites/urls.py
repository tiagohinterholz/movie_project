from django.urls import path
from apps.favorites.views.favorite_view import (
    FavoriteListCreateView,
    FavoriteDeleteView,
)

urlpatterns = [
    path("", FavoriteListCreateView.as_view(), name="favorite-list-create"),
    path("<uuid:pk>/", FavoriteDeleteView.as_view(), name="favorite-delete"),
]
