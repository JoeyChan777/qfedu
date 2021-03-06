from django.shortcuts import render, get_object_or_404
from .models import BlogArticles


def blog_title(request):
    blogs = BlogArticles.objects.all()
    return render(request, 'blog/titles.html', {'blogs': blogs})


def blog_content(request, article_id):
    # blog = BlogArticles.objects.get(id=article_id)
    article = get_object_or_404(BlogArticles, id=article_id)
    return render(request, 'blog/content.html', {'article': article})
