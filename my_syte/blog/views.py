from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse('Главная страница блога')

def posts(request):
    return HttpResponse(f'все посты блога')
def post_name(request, name_post):
    return HttpResponse(f'Информация о посте {name_post}')

def post_number(request, number_post):
    return HttpResponse(f'Здесь содержится информация о посте под номером {number_post}')
