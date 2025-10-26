from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
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


class  FavoriteShareGenerateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, share_uuid):
        result = favorite_list_service.get_share_link(request.user, request)
        return Response(result, status=200)


class FavoriteShareView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, share_uuid):
        favorite_list = favorite_list_service.get_share_uuid(share_uuid)
        if not favorite_list.exists():
            return Response({"detail": "Link inválido ou expirado."}, status=404)
        serializer = FavoriteListSerializer(favorite_list, many=True)
        return Response(serializer.data, status=200)