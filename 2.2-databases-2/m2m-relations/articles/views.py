from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    ordering = '-published_at'
    all_articles = Article.objects.order_by(ordering)
    context = {
        'object_list': all_articles
    }

    return render(request, template, context)
