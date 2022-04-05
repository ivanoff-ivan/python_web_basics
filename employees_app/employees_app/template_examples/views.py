from django.shortcuts import render
import random


def index(request):
    context = {
        'filesize': 9999999999,
        'number': random.randint(1, 400),
        'numbers': [123, 321, 200],
        'title': 'Employees list',
    }
    return render(request, 'templates_examples/index.html', context)
