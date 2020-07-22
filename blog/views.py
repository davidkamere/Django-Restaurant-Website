from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Post


# Create your views here.
def index(request):
    """The home page for mama's plate"""
    return render(request, 'blog/index.html')


def blog(request):
    """The blog for Mama's plate"""
    entry_list = Post.objects.order_by('-date_added')
    paginator = Paginator(entry_list, 5)
    page = request.GET.get('page')
    entries = paginator.get_page(page)
    context = {'posts': entries}
    return render(request, 'blog/blog.html', context)


# posts
def post(request, entry_id):
    entry = Post.objects.get(id=entry_id)
    context = {'entry': entry}
    return render(request, 'blog/post.html', context)


def about(request):
    """The about for Mama's plate"""

    return render(request, 'blog/about.html')
