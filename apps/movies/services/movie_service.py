import os
import requests


class MovieService:
    def __init__(self):
        self.base_url = "https://api.themoviedb.org/3"
        self.api_key = os.getenv("TMDB_API_KEY")

    def search(self, query, page=1, language="pt-BR"):
        url = f"{self.base_url}/search/movie"
        params = {
            "api_key": self.api_key,
            "query": query,
            "page": page,
            "language": language,
            "include_adult": "false",
        }
        response = requests.get(url, params=params)
        return response.json()

    def details(self, movie_id, language="pt-BR"):
        url = f"{self.base_url}/movie/{movie_id}"
        params = {
            "api_key": self.api_key,
            "language": language,
        }
        response = requests.get(url, params=params)
        return response.json()

movie_service = MovieService()