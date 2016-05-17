# from rest_framework import serializers
# from .models import Board, Column, Cards
# from rest_framework import serializers
# from django.contrib.auth.models import User
#
#

# class ColumnSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Column
#         fields=('board', 'name', 'order')
#
# class CardsSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Cards
#         fields = ('column', 'name', 'order')


from django.contrib.auth.models import User
from rest_framework import serializers
from boards.models import Board, Column, Cards

class UserSerializer(serializers.HyperlinkedModelSerializer):

    boards = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Board.objects.all(),
    )
    class Meta:
        model = User
        fields = ('username', 'id')


class BoardSerializer(serializers.HyperlinkedModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Board
        fields = ('name', 'description', 'user_obj', 'owner')
