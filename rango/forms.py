# 书7.2章中加入
from django import forms
from rango.models import Page, Category
# We could add these forms to views.py, but it makes sense to split them off into their own file.

class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=Category.Name_MAX_LENGTH, help_text="Please enter the category name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False) # 该字段也被隐藏，且指明该字段不是必须的。这里没有设置初始值，
    # 因为我们之前在admin中设定过slug字段可以自动生成。

    class Meta:
        model = Category
        fields = ('name',) # fields指定表单中包括哪些字段，也就是用户可见的


class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=Page.TITLE_MAX_LENGTH, help_text="Please enter the title of the page.")
    url = forms.URLField(max_length=200, help_text="Please enter the URL of the page.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0) # 这里的小组件是将该字段设为隐藏值，用户无法输入，但是设置了初始值

    class Meta:
        model = Page
        exclude = ('category',) # exclude指定表单中排除哪些字段，也就是用户不可见的

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')

        if url and not url.startswith('http://'):
            url = f'http://{url}'
            cleaned_data['url'] = url

        return cleaned_data