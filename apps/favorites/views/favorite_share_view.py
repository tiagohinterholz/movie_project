from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from django.urls import reverse

from apps.favorites.serializers.favorite_serializer import FavoriteSerializer
from apps.favorites.services.favorite_list_service import favorite_list_service
from apps.favorites.repositories.favorite_list_repository import favorite_list_repository


class FavoriteShareGenerateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, favorite_list_id):
        favorite_list = favorite_list_service.list_by_user(request.user, favorite_list_id)
        share_link = request.build_absolute_uri(
            reverse("favorite-share", kwargs={"share_uuid": favorite_list.share_uuid})
        )
        return Response({"share_link": share_link}, status=status.HTTP_200_OK)


class FavoriteShareView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, share_uuid):
        favorite_list = favorite_list_repository.get_by_share_uuid(share_uuid)
        if not favorite_list:
            return Response({"detail": "Link inválido ou expirado."}, status=status.HTTP_404_NOT_FOUND)

        favorites = favorite_list.favorites.all()
        serializer = FavoriteSerializer(favorites, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
