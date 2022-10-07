from django.shortcuts import render
from django.http import HttpResponse

def index(request):    
    return HttpResponse('Главная страница')

def group_posts(request, group_condition):
    return HttpResponse(f'Страница с постами, сгруппированными по признаку: {group_condition}')
