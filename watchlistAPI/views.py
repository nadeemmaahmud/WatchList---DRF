from django.shortcuts import render
from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from . permissions import IsAdminOrReadOnly, IsUserObjectOrReadOnly
from . models import WatchList, WatchCategory, Reviews
from . serializers import WatchListSerializer, WatchCategorySerializer, ReviewSerializer
from . paginations import WatchListCursorPagination

class WatchCategoryView(viewsets.ModelViewSet):
    queryset = WatchCategory.objects.all()
    serializer_class = WatchCategorySerializer
    permission_classes = [IsAdminOrReadOnly]

class WatchListView(viewsets.ModelViewSet):
    queryset = WatchList.objects.all()
    serializer_class = WatchListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'category']
    pagination_class = WatchListCursorPagination
    permission_classes = [IsAdminOrReadOnly]

class ReviewView(viewsets.ModelViewSet):
    queryset = Reviews.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsUserObjectOrReadOnly, permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)