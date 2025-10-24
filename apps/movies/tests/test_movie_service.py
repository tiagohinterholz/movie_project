import pytest
from apps.movies.services.movie_service import movie_service


@pytest.mark.django_db
def test_search_returns_results():
    result = movie_service.search("Matrix")
    assert "results" in result
    assert len(result["results"]) > 0


@pytest.mark.django_db
def test_movie_details_returns_data():
    movie_id = 603
    result = movie_service.details(movie_id)
    assert result["id"] == movie_id
    assert "title" in result
