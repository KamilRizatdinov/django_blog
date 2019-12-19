from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from blog.models import Post


# Create your views here.
def index(request):
    latest_posts_list = Post.objects.order_by('-publication_date')[:5]
    context = {'latest_posts_list': latest_posts_list}
    return render(request, 'blog/index.html', context)


def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {'post': post}
    return render(request, 'blog/detail.html', context)


def read(request):
    post = Post.objects.get(pk=request.POST['post_id'])
    post.views += 1
    post.save()
    return HttpResponseRedirect(reverse('blog:index'))
