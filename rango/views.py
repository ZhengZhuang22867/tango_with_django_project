from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    # 书4.1和4.2加入
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    # Spoiler: you don't need to pass a context dictionary here.
    # 书第四章课后练习
    return render(request, 'rango/about.html')
