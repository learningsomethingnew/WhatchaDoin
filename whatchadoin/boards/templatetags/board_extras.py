from django import template

register = template.Library()

from boards.models import Cards


@register.filter(name='get_card')
def get_card(col_id):
    return Cards.objects.filter(column=col_id).order_by('order')