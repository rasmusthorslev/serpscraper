from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=255)
    # Add more fields as needed (email, contact info, etc.)

    def __str__(self):
        return self.name

class Keyword(models.Model):
    name = models.CharField(max_length=255)
    clients = models.ManyToManyField(Client, related_name='keywords')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class RankResult(models.Model):
    keyword = models.ForeignKey(Keyword, on_delete=models.CASCADE)
    domain = models.CharField(max_length=255)
    position = models.IntegerField()
    checked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.keyword} - {self.domain} - {self.position}"