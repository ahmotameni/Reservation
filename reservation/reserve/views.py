from django.shortcuts import render
from .models import Food


def menu(request):
    foods = Food.objects.all()
    context = {'foods': foods}
    return render(request, 'reserve/menu.html', context)
