from django.http import HttpResponse


def index(request):
    return HttpResponse('Главная страница')


def posts(request):
    return HttpResponse('Все посты блога')


def post_info(request, name_post):
    return HttpResponse(f'Информация о посте {name_post}')


def post_number(request, number_post: int):
    return HttpResponse(f'Здесь содержится информация о посте под номером {number_post}')
