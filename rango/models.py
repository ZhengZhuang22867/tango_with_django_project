from django.db import models
# 书5.3章创建category和page两个模型
from django.template.defaultfilters import slugify


class Category(models.Model):
    Name_MAX_LENGTH = 128 # 书第7章课后练习中要求加入该变量
    name = models.CharField(max_length=Name_MAX_LENGTH, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    # 书6.3章中加入，使得分类的别名无法重复，对别名为空的分类会有影响
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Page(models.Model):
    TITLE_MAX_LENGTH = 128 # 书第7章课后练习中要求加入该变量
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=TITLE_MAX_LENGTH)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title