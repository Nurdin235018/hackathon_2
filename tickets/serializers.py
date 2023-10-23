from rest_framework import serializers
from .models import Tickets, Category, Flight
from review.serializers import *
from django.db.models import Avg


class TicketsSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.name')

    class Meta:
        model = Tickets
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class FlightSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.name')
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Flight
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['comments'] = CommentSerializer(instance.comments.all(), many=True).data
        rep['rating'] = instance.ratings.aggregate(Avg('rating'))['rating__avg']
        rep['likes'] = instance.likes.count()
        return rep


class RecommendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tickets
        fields = '__all__'