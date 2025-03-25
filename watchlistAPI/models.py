from django.db import models
from django.contrib.auth.models import User

class WatchCategory(models.Model):
    name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.name
    
class WatchList(models.Model):
    title = models.CharField(max_length=32)
    category = models.ForeignKey(WatchCategory, on_delete=models.SET_NULL, null=True)
    release_date = models.DateField()

    def __str__(self):
        return self.title
    
class Reviews(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.TextField()
    rating = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    watchlist = models.ForeignKey(WatchList, on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return self.review[:10]