from django.shortcuts import render
from .models import Food, Restaurant


def menu(request):
    foods = Food.objects.all()
    restaurant = Restaurant.objects.get(id=1)
    context = {'foods': foods,
               'restaurant': restaurant}
    return render(request, 'reserve/menu.html', context)


def homepage(request):
    restaurant = Restaurant.objects.get(id=1)
    context = {'restaurant': restaurant}
    return render(request, 'reserve/index.html', context)
