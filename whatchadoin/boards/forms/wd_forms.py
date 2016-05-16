from django import forms


class BoardsForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        label="Project Name",
        required=True,
    )

    col_description = forms.CharField(
        required=False,
        label="Description"
    )


class ColumnsForm(forms.Form):
    col_name = forms.CharField(
        max_length=255,
        label="Add a list",
        required=True,
    )


class CardsForm(forms.Form):
    card_name = forms.CharField(
        max_length=255,
        label="Task Name",
        required=True,
    )

    col_id = forms.IntegerField(widget=forms.HiddenInput())