from django.shortcuts import render


# Create your views here.
def index(request):
    """The home page for mama's plate"""
    return render(request, 'blog/index.html')


def blog(request):
    """The blog for Mama's plate"""

    return render(request, 'blog/blog.html')


def about(request):
    """The about for Mama's plate"""

    return render(request, 'blog/about.html')
