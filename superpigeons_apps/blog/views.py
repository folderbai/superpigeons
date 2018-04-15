from django.shortcuts import render
from superpigeons_apps.user.models import UserInfo
from superpigeons_apps.blog.forms import WriteArticle
from superpigeons_apps.blog.models import Article
# Create your views here.


def blog_index(request):
    article = Article.objects.values('id', 'auther__userinfo__nickname', 'auther_id', 'title').order_by('-mod_date')
    for i in article:
        print(i)
    context = dict()
    context['article'] = article
    return render(request, 'blog_index.html', context)


def blog_article(request, artid):
    article = Article.objects.get(id=artid)
    userinfo = UserInfo.objects.get(user_id=article.auther_id)
    context = dict()
    context['article'] = article
    context['userinfo'] = userinfo
    return render(request, 'blog_article.html', context)


def blog_write(request):
    form = WriteArticle()
    userinfo = UserInfo.objects.get(user__username='bailidf')
    context = dict()
    context['t'] = 'aaaa'
    context['userinfo'] = userinfo
    context['form'] = form
    return render(request, 'blog_write.html', context)


def test(request):
    return render(request, 'test.html')


