from rest_framework import serializers
from .models import Board, Column, Cards



class BoardSerializer(serializers.Serializer):
    class Meta:
        model = Board
        fields = ('name', 'description', 'user_obj')

class ColumnSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Column
        fields=('board', 'name', 'order')

class CardsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cards
        fields = ('column', 'name', 'order')