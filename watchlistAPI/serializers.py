from rest_framework import serializers
from . models import WatchList, WatchCategory, Reviews

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = "__all__"

        extra_kwargs = {
            'rating': {
                'max_value': 10,
                'min_value': 1,
                'error_messages': {
                    'max_value': 'Rating must be less than 10',
                    'min_value': 'Rating must be greater than 1',
                },
            },
        }

class WatchListSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    class Meta:
        model = WatchList
        fields = "__all__"

class WatchCategorySerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only=True)
    class Meta:
        model = WatchCategory
        fields = "__all__"