from django.shortcuts import render
from rest_framework import viewsets, permissions
from . permissions import IsAdminOrReadOnly, IsUserObjectOrReadOnly
from . models import WatchList, WatchCategory, Reviews
from . serializers import WatchListSerializer, WatchCategorySerializer, ReviewSerializer

class WatchCategoryView(viewsets.ModelViewSet):
    queryset = WatchCategory.objects.all()
    serializer_class = WatchCategorySerializer
    permission_classes = [IsAdminOrReadOnly]

class WatchListView(viewsets.ModelViewSet):
    queryset = WatchList.objects.all()
    serializer_class = WatchListSerializer
    permission_classes = [IsAdminOrReadOnly]

class ReviewView(viewsets.ModelViewSet):
    queryset = Reviews.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsUserObjectOrReadOnly, permissions.IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)