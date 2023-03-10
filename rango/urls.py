from django.urls import path
from rango import views

app_name = 'rango'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('index/', views.index, name='index'), # 这个是自己加的，因为比较符合书写和思维习惯
    path('about/', views.about, name = 'about'),
    path('category/<slug:category_name_slug>/',
         views.show_category, name='show_category'),
    path('add_category/', views.add_category, name='add_category'),# 书7.2章中加入
    path('category/<slug:category_name_slug>/add_page/',
         views.add_page, name='add_page'), # 书第7章课后练习中加入
]