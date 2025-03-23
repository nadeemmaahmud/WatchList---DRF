from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WatchCategoryView, WatchListView, ReviewView

router = DefaultRouter()
router.register('category', WatchCategoryView, basename='category')
router.register('watchlist', WatchListView, basename='watchlist')
router.register('review', ReviewView, basename='review')

urlpatterns = [
    path('', include(router.urls)),
]
