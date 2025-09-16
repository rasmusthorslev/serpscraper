from django.db import models

class Keyword(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class RankResult(models.Model):
    keyword = models.ForeignKey(Keyword, on_delete=models.CASCADE, related_name='results')
    domain = models.CharField(max_length=255)
    position = models.IntegerField()
    checked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.domain} - {self.keyword.name} ({self.position})"