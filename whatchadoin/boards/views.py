from django.shortcuts import render, redirect, get_object_or_404


# Require login
from django.contrib.auth.decorators import login_required
from .models import Board, Column, Cards
from .forms.wd_forms import BoardsForm, ColumnsForm, CardsForm

#API Stuff
from rest_framework import viewsets


@login_required(login_url='/login/')
def boards_home(request):

    user_boards = Board.get_user_boards(request.user.id)

    # load boards
    if request.method == 'GET':
        form = BoardsForm()
    else:
        # take in the form data
        form = BoardsForm(request.POST)

        # test form data
        if form.is_valid():

            name = form.cleaned_data['name']
            description = form.cleaned_data['description']

            post = Board.objects.create(
                name=name,
                description=description,
                user_obj_id=request.user.id,
            )


    return render(
        request,
        'boards/user_boards.html',
        {
            'form': form,
            'boards': user_boards,
        }
    )


@login_required(login_url='/login')
def board(request, board_id):

    columns = Column.get_columns(board_id)

    """HOW DO YOU LINK CARDS TO COLUMNS?"""

    cards = Cards.get_cards(columns)

    # print(cards)


    col_form = ""
    card_form = ""

    # load forms
    if request.method == 'GET':
        col_form = ColumnsForm()
        card_form = CardsForm()

    # If user is posting forms. Tests which form it is
    elif request.method == 'POST' and 'new_list' in request.POST:
        col_form = ColumnsForm(request.POST)
        # test form data
        if col_form.is_valid():
            col_name = col_form.cleaned_data['col_name']

            post = Column.objects.create(
                board_id=board_id,
                name=col_name,
            )

    elif request.method == 'POST' and 'new_card' in request.POST:
        card_form = CardsForm(request.POST)

        # test form data
        if card_form.is_valid():
            col_id = card_form.cleaned_data['col_id']
            card_name = card_form.cleaned_data['card_name']
            post = Cards.objects.create(
                column_id=col_id,
                name=card_name,
            )

    context = {
        'columns': columns,
        'colform': col_form,
        'cardform': card_form,
    }


    return render(
        request,
        'boards/board.html',
        context
    )


class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board