from django.template import Library
from django.utils.html import escape
from django.utils.safestring import SafeString
from surveys.models import Survey
from django.db.models import Avg

register = Library()


@register.simple_tag
def product_format(product, short=False):
    if short:
        return f'{product.name}'
    return f'{product.name} ({product.price})'


@register.filter
def attr_as_p(obj, attrname):
    label = escape(attrname.capitalize())
    value = escape(getattr(obj, attrname))
    return SafeString(f'<p><strong>{label}:</strong> {value}</p>')


@register.filter
def average_rating(product, rate_number: str):
    if Survey.objects.all().count() == 0:
        return f'No surveys'
    else:
        return round(Survey.objects.filter(product_id=product.id).aggregate(Avg(rate_number))
                    ['rate_' + rate_number[-1] + '__avg'], 1)


@register.filter
def product_full_average(product):
    rating = []
    if Survey.objects.all().count() == 0:
        return f'No surveys'
    else:
        for num in range(5):
            rating.append(average_rating(product, 'rate_' + str(num + 1)))
        return round(sum(rating)/len(rating), 1)
