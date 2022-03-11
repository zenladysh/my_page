from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
days_dict = {
    1: 'monday',
    2: 'tuesday',
    3: 'wednesday',
    4: 'tuesday',
    5: 'friday',
    6: 'saturday',
    7: 'sunday',
}


def get_info_about_day_of_week(request, day_of_week: str):
    if day_of_week in days_dict.values():
        return HttpResponse(f'To do list on {day_of_week}')
    else:
        return HttpResponseNotFound(f'Unknown day of week - {day_of_week}')


def get_info_about_day_of_week_by_number(request, day_of_week: int):
    if day_of_week in days_dict.keys():
        day = days_dict[day_of_week]
        redirect_url = reverse("week_name", args=(day,))
        return HttpResponseRedirect(redirect_url)
    else:
        return HttpResponseNotFound(f'Unknown day of week - {day_of_week}')
