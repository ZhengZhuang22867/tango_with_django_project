from django import template
from rango.models import Category

register = template.Library()

@register.inclusion_tag('rango/categories.html')# 对这个非常困惑，尤其是和下面的方法的关系。再就是current_category不知道是哪来的
def get_category_list(current_category=None):
    return {'categories':Category.objects.all(),
            'current_category':current_category}