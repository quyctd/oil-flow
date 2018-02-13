from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post
from django.views.generic import DetailView, ListView
from django.db.models import Q
from taggit.models import Tag


# Create your views here.

class PostListView(ListView):
    model = Post
    def get_queryset(self):
        return Post.objects.all()


def post_detail(request, pk):
    post = get_object_or_404(Post, pk = pk)
    post.hits = post.hits + 1
    post.save()
    context = {
        "post": post,
    }
    return render(request, "blog/post_detail.html", context=context)

def index(request):
    query = request.GET.get("q")
    tags = Tag.objects.all()
    post_list= []
    if query:
        post_list = Post.objects.all()
        post_list = post_list.filter(
            Q(title__icontains = query)|
            Q(answer__icontains = query)|
            Q(tags__name__icontains = query)
        ).distinct()
    else:
        post_list = Post.objects.all()[:3]
    context = {
        "post_list": post_list,
        "query": query,
        "tags": tags,
    }

    return render(request, 'blog/homepage.html', context = context)
