from django.urls import path
from teacherChat import views

app_name = 'teacherChat'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('goods/', views.goods_list, name='goods_list'),
]
