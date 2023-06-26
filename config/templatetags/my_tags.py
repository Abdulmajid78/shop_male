from django import template

register = template.Library()


@register.simple_tag()
def get_current_price(request, index):
    data = request.GET.get('price')
    if data:
        return data.split(';')[index]
    return 'null'
