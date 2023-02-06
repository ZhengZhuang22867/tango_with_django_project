# 书5.7章加入，作为向数据库输入测试数据的脚本
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category,Page

def populate():
    python_pages=[
        {'title':'Offical Python Tutorial',
         'url':'http://docs.python.org/3/tutorial/',
         'views':114,},
        {'title':'How to Think like a Computer Scientist',
         'url':'http://www.greenteapress.com/thinkpython/',
         'views':53,},
        {'title':'Learn Python in 10 Minutes',
         'url':'http://www.korokithakis.net/tutorials/python/',
         'views':20} ]

    django_pages = [
        {'title':'Official Django Tutorial',
         'url':'https://docs.djangoproject.com/en/2.1/intro/tutorial01/',
         'views':32,},
        {'title': 'Django Rocks',
         'url':'http://www.djangorocks.com/',
         'views':12,},
        {'title':'How to Tango with Django',
         'url':'http://www.tangowithdjango.com/',
         'views':1258,} ]

    other_pages = [
        {'title': 'Bottle',
         'url':'http://bottlepy.org/docs/dev/',
         'views':54,},
        {'title': 'Flask',
         'url': 'http://flask.pocoo.org',
         'views':64,} ]

    # 自己加的
    java_pages=[
        {'title':'Java Tutorial for Beginners',
         'url':'https://www.youtube.com/watch?v=eIrMbAQSU34',
         'views':8590000,},
        {'title':'Learn Java Programming',
         'url':'https://www.programiz.com/java-programming',
         'views':27981,}]

    # 第5章课后练习题修改部分2：在内部字典中加入views和likes两个属性
    cats = {'Python': {'pages':python_pages,'views':128,'likes':64},
            'Django': {'pages':django_pages,'views':64,'likes':32},
            'Other Frameworks':{'pages':other_pages,'views':32,'likes':16},
            'Java':{'pages':java_pages,'views':79992,'likes':8990},
            }

    # 第5章课后练习题修改部分3：增加add_cat方法的参数（一开始时只有cat）
    for cat, cat_data in cats.items():
        c = add_cat(cat,views=cat_data['views'],likes=cat_data['likes'])# add_cat方法调用
        for p in cat_data['pages']:
            add_page(c, p['title'], p['url'], views=p['views']) # add_page方法调用

    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(f'- {c}: {p}')

def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.views=views
    p.save()
    return p

#第5章课后练习题修改部分1：加入views，likes参数，并在方法体中加入赋值部分
def add_cat(name,views=0,likes=0):
    c = Category.objects.get_or_create(name=name)[0]
    c.views = views
    c.likes = likes
    c.save()
    return c

# 这个__name__=='__main__'的作用是，当这个文件被作为独立的python脚本文件时才
# 会被执行。如果是作为模块导入则不执行，因为导入时为了访问模块中的类或函数。
if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()