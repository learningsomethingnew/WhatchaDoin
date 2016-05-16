from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Board(models.Model):
    user_obj = models.ForeignKey(User)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    @staticmethod
    def get_user_boards(user_id):
        if Board.objects.filter(user_obj_id=user_id):
            return Board.objects.filter(user_obj_id=user_id)

    def __str__(self):
        return "Printing Board of {}".format(self.name)


class Column(models.Model):
    board = models.ForeignKey(Board)
    name = models.CharField(max_length=255)
    order = models.IntegerField(default=lambda: Column.get_latest_id())

    """ASK BRYCE. BETTER WAY?
        What about a non-static. How would you call it?"""

    @staticmethod
    def get_latest_id():
        try:
            return Column.objects.latest('id').id+1
        except:
            return 1

    @staticmethod
    def get_columns(board_id):
        if Column.objects.filter(board=board_id):
            return Column.objects.filter(board=board_id).order_by('order')

    def update_column_order(self, board_id):
        pass


class Cards(models.Model):
    column = models.ForeignKey(Column, related_name='cards_per_column')
    name = models.CharField(max_length=255)
    order = models.IntegerField(default=lambda: Column.get_latest_id())

    @staticmethod
    def get_latest_id():
        try:
            return Cards.objects.latest('id').id + 1
        except:
            return 1

    @staticmethod
    def get_cards(columns):
        if len(columns)>0:
            column_cards_dict = {}
            for col in columns:
                column_cards_dict[col.name] = Cards.objects.filter(column=col.id)
                print(column_cards_dict[col.name])
        return column_cards_dict

