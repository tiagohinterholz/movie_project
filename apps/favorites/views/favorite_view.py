from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from apps.favorites.serializers.favorite_serializer import FavoriteSerializer
from apps.favorites.services.favorite_service import favorite_service


class FavoriteListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        favorites = favorite_service.list_favorites(request.user)
        serializer = FavoriteSerializer(favorites, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        favorite = favorite_service.add_favorite(request.user, request.data)
        serializer = FavoriteSerializer(favorite)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class FavoriteDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        result = favorite_service.remove_favorite(request.user, pk)
        return Response(result, status=status.HTTP_204_NO_CONTENT)
