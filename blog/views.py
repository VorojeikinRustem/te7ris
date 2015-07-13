# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Article


dates = []


def archive():
    all = Article.objects.all()
    l = len(all)
    for i in range(l):
        if all[i].article_date not in dates:
            dates.append(all[i].article_date)
            print(str(all[i].article_date))


def articles(request, month=0, year=0, page_number=1):

    context = {}
    if month and year:
        all_articles = [Article.objects.all()[i] for i in range(len(Article.objects.all())) if Article.objects.all()[i].article_date.year==int(year) and Article.objects.all()[i].article_date.month==int(month)]
    else:
        all_articles = Article.objects.all()

    archive()

    page_number = request.GET.get('page')
    paginator = Paginator(all_articles, 2)
    try:
        context['articles'] = paginator.page(page_number)
    except PageNotAnInteger:
        context['articles'] = paginator.page(1)
    except EmptyPage:
        context['articles'] = paginator.page(paginator.num_pages)
    context['dates'] = dates

    return render(request, 'blog_articles.html', context)
# [i for i in client.database_names() if i not in ['test', 'dashboard', 'local', 'admin']]


def article(request, article_id):
    context = {}
    archive()
    context['dates'] = dates
    context['article'] = Article.objects.get(pk=article_id)
    return render(request, 'blog_article.html', context)


def about(request):
    context = {}
    archive()
    context['dates'] = dates
    return render(request, 'blog_about.html', context)
