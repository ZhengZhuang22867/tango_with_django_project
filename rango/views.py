from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category # 第6.2章加入 导入Category模型
from rango.models import Page# 第6.3章加入 导入Page模型

def index(request):
    # 书4.1和4.2加入
    # context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
    # return render(request, 'rango/index.html', context=context_dict)

    # 书6.2加入
    category_list = Category.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-views')[:5]
    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list
    context_dict['pages'] = page_list
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    # Spoiler: you don't need to pass a context dictionary here.
    # 书第四章课后练习
    return render(request, 'rango/about.html')

# 第6.3章加入
def show_category(request, category_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None
    return render(request,'rango/category.html',context=context_dict)
