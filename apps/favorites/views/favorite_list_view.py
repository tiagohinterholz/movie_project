from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from apps.favorites.serializers.favorite_list_serializer import FavoriteListSerializer
from apps.favorites.services.favorite_list_service import favorite_list_service


class FavoriteListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        favorite_lists = favorite_list_service.all_lists_by_user(request.user)
        serializer = FavoriteListSerializer(favorite_lists, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        name = request.data.get("name")
        favorite_list = favorite_list_service.create(request.user, name)
        serializer = FavoriteListSerializer(favorite_list)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class FavoriteListDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, list_id):
        favorite_list = favorite_list_service.list_by_user(request.user, list_id)
        serializer = FavoriteListSerializer(favorite_list)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, list_id):
        name = request.data.get("name")
        updated_list = favorite_list_service.update(request.user, list_id, name)
        serializer = FavoriteListSerializer(updated_list)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, list_id):
        favorite_list_service.delete(request.user, list_id)
        return Response(status=status.HTTP_204_NO_CONTENT)
