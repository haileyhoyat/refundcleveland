from django.shortcuts import render
from django.shortcuts import HttpResponse
import json
from django.conf import settings
import os


def home(request):
    with open(os.path.join(settings.BASE_DIR, 'static/data/2020-mayors-estimate-fullgeneralfund.json')) as file:
        json_file = json.load(file)

    return render(request, 'home.html', {
        'home': True,
        'data': json_file,
        'body_classes': 'home colored-bg'
    })


def change_budget(request):
    with open(os.path.join(settings.BASE_DIR, 'static/data/2020-mayors-estimate-fullgeneralfund.json')) as file:
        json_file = json.load(file)
        
    return render(request, 'change-the-budget.html', {
        'change_budget': True,
        'data': json_file,
        'body_classes': 'change-the-budget'
    })

