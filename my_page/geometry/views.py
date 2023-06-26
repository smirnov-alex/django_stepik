# from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


def get_rectangle_area(request, width: int, height: int):
    return HttpResponseRedirect(reverse('rectangle', args=[width, height]))


def rectangle(request, width: int, height: int):
    area = width * height
    return HttpResponse(f'Площадь прямоугольника размером {width}X{height} равна {area}')


def get_square_area(request, width: int):
    return HttpResponseRedirect(reverse('square', args=[width]))


def square(request, width: int):
    area = width * width
    return HttpResponse(f'Площадь квадрата размером {width}X{width} равна {area}')


def get_circle_area(request, radius: int):
    return HttpResponseRedirect(reverse('circle', args=[radius]))


def circle(request, radius: int):
    area = radius ** 2 * 3.14
    return HttpResponse(f'Площадь круга радиусом {radius} равна {area}')
