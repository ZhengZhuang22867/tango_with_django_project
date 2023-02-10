from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from teacherChat.models import Goods


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('goods_list')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'teacherChat/login.html')

@login_required
def goods_list(request):
    goods = Goods.objects.all()
    return render(request, 'teacherChat/goods_list.html', {'goods': goods})


