from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from apps.favorites.serializers.favorite_serializer import FavoriteSerializer
from apps.favorites.services.favorite_list_service import favorite_list_service
from apps.favorites.services.favorite_service import favorite_service


class FavoriteCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, favorite_list_id):
        favorites = favorite_service.list_favorites(request.user, favorite_list_id)
        serializer = FavoriteSerializer(favorites, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, favorite_list_id):
        favorite_list = favorite_list_service.list_by_user(request.user, favorite_list_id)
        
        favorite = favorite_service.add_favorite(request.user, favorite_list.id, request.data)
        serializer = FavoriteSerializer(favorite)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class FavoriteDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, favorite_list_id, favorite_id):
        result = favorite_service.remove_favorite(request.user, favorite_list_id, favorite_id)
        return Response(result, status=status.HTTP_204_NO_CONTENT)