from rest_framework import serializers
from .models import Tickets, Tag, Category


class TicketsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tickets
        fields = '__all__'

    '''Dont know for what is this'''
    def create(self, validated_data):
        user = self.context.get('request').user
        tags = validated_data.pop('tags', [])
        ticket = self.Meta.model.objects.create(author=user, **validated_data)
        ticket.tags.add(*tags)
        return ticket


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = '__all__'