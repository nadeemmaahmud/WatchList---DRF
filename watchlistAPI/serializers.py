from rest_framework import serializers
from . models import WatchList, WatchCategory, Reviews

class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    
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

class WatchCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = WatchCategory
        fields = "__all__"

class WatchListSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()

    reviews = ReviewSerializer(many=True, read_only=True)
    class Meta:
        model = WatchList
        fields = "__all__"