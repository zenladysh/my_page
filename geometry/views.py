import re
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound

figures = ('rectangle', 'square', 'circle',)

def get_rectangle_area(request, width: int, height: int):
    return HttpResponse(f'Площадь прямоугольника размером {width}х{height} равна {width * height} --- {request}')


def get_square_area(request, width: int):
    return HttpResponse(f'Площадь квадрата размером {width}х{width} равна {width ** 2}')


def get_circle_area(request, radius: int):
    return HttpResponse(f'Площадь круга радиусом {radius} равна {3.14 * radius ** 2}')

def get_figure_area(request, args):
    figure_name = re.search(r'\w*_(\w)_\w*', args[0])
    return HttpResponse(f'{figure_name}')
    # if figure_name in figures:
    #     if len(args) == 1:
    #         return HttpResponseRedirect(f'/{figure_name}/{args[0]}')
    #     else:
    #         return HttpResponseRedirect(f'/{figure_name}/{args[0]}/{args[1]}')
    # return HttpResponseNotFound(f'Фигура {figure_name} не определена')

