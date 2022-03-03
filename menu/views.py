from django.shortcuts import render
from blog.models import Post


# Create your views here.
def menu(request):
    """The menu for Mama's plate"""
    entries = Post.objects.order_by('title')
    context = {'posts': entries}
    return render(request, 'menu/menu.html', context)




