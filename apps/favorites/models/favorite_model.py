import uuid
from django.db import models


class Favorite(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    favorite_list = models.ForeignKey(
        "FavoriteList", on_delete=models.CASCADE, related_name="favorites"
    )
    tmdb_id = models.PositiveIntegerField()
    title = models.CharField(max_length=255)
    original_title = models.CharField(max_length=255, blank=True, null=True)
    overview = models.TextField(blank=True, null=True)
    poster_path = models.CharField(max_length=255, blank=True, null=True)
    backdrop_path = models.CharField(max_length=255, blank=True, null=True)
    release_date = models.CharField(max_length=20, blank=True, null=True)
    vote_average = models.FloatField(blank=True, null=True)
    vote_count = models.PositiveIntegerField(blank=True, null=True)
    genres = models.JSONField(blank=True, null=True)
    runtime = models.PositiveIntegerField(blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("favorite_list", "tmdb_id")
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.user.email} - {self.title}"