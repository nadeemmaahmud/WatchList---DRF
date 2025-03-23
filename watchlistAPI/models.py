from django.db import models

class WatchCategory(models.Model):
    name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.name
    
class WatchList(models.Model):
    title = models.CharField(max_length=32)
    category = models.ForeignKey(WatchCategory, on_delete=models.SET_NULL, null=True, related_name='watchlist')
    release_date = models.DateField()
    is_watched = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
class Reviews(models.Model):
    review = models.TextField()
    rating = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    watchlist = models.ForeignKey(WatchList, on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return self.review[:10]