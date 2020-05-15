from django.shortcuts import render
from menu.models import Category, SubCategory, Item


# Create your views here.
def menu(request):
    """The menu for Mama's plate"""
    items = Item.objects.order_by('dish')
    context = {'items': items}
    return render(request, 'menu/menu.html', context)

