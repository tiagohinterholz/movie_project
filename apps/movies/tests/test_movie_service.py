from django.test import TestCase
from apps.movies.services.movie_service import movie_service


class MovieServiceTest(TestCase):
    def test_search_returns_results(self):
        result = movie_service.search("Matrix")
        self.assertIn("results", result)
        self.assertGreater(len(result["results"]), 0)

    def test_movie_details_returns_data(self):
        movie_id = 603
        result = movie_service.details(movie_id)
        self.assertEqual(result["id"], movie_id)
        self.assertIn("title", result)
