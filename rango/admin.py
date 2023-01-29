from django.contrib import admin
from rango.models import Category,Page

# 第5章练习题加入部分，让pageadmin界面加入分类
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

# 书6.3章中加入，使在admin界面中添加新的category时，自动完成别名的输入
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
