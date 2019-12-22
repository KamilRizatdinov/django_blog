from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.utils import timezone
import requests
import json

from blog.models import Post


# Create your views here.
def index(request):
    latest_posts_list = Post.objects.order_by('-publication_date', '-views')
    for post in latest_posts_list:
        post.text = post.text[:50]+'..'
    context = {'latest_posts_list': latest_posts_list}
    return render(request, 'blog/index.html', context)


def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {'post': post}
    return render(request, 'blog/detail.html', context)


def contributors(request):
    r = requests.get("https://api.github.com/repos/KamilRizatdinov/django_blog/stats/contributors")
    if r.status_code != 200:
        return HttpResponse('Something went wrong!')
    json_data = json.loads(r.text)
    contributors = [
        {'total': contributor['total'],
         'login': contributor['author']['login'],
         'avatar': contributor['author']['avatar_url'],
         'profile_url': contributor['author']['html_url']}
        for contributor in json_data
    ]
    context = {'contributors': contributors}
    return render(request, 'blog/contributors.html', context)


def read(request):
    try:
        post = Post.objects.get(pk=request.POST['post_id'])
        post.views += 1
        post.save()
    except (KeyError, Post.DoesNotExist):
        return HttpResponseRedirect(reverse('blog:index'))
    return HttpResponseRedirect(reverse('blog:index'))


def publish(request):
    post = Post(
        header=request.POST['header'],
        text=request.POST['text'],
        publication_date=timezone.datetime.now()
    )
    post.save()
    return HttpResponseRedirect(reverse('blog:index'))
