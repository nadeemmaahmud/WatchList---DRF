from django.shortcuts import render
from rest_framework import viewsets
from . models import WatchList, WatchCategory, Reviews
from . serializers import WatchListSerializer, WatchCategorySerializer, ReviewSerializer

class WatchCategoryView(viewsets.ModelViewSet):
    queryset = WatchCategory.objects.all()
    serializer_class = WatchCategorySerializer

class WatchListView(viewsets.ModelViewSet):
    queryset = WatchList.objects.all()
    serializer_class = WatchListSerializer

class ReviewView(viewsets.ModelViewSet):
    queryset = Reviews.objects.all()
    serializer_class = ReviewSerializer