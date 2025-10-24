from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.movies.services.movie_service import movie_service


class MovieSearchView(APIView):
    def get(self, request):
        query = request.query_params.get("q")
        page = request.query_params.get("page", 1)

        if not query:
            return Response(
                {"error": "O parâmetro 'q' é obrigatório."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        data = movie_service.search(query=query, page=page)
        return Response(data, status=status.HTTP_200_OK)


class MovieDetailView(APIView):
    def get(self, request, movie_id):
        data = movie_service.details(movie_id=movie_id)
        return Response(data, status=status.HTTP_200_OK)
