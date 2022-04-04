from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from collections import namedtuple
from datetime import datetime as dt
from django.template.loader import render_to_string

Zodiac = namedtuple("Zodiac", "description start_date end_date")
zodiac_dict = {
    "aries": Zodiac("Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля)",
                    "21-03", '20-04'),
    "taurus": Zodiac("Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая)",
                     "21-04", "21-05"),
    "gemini": Zodiac("Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня)",
                     "22-05", "21-06"),
    "cancer": Zodiac("Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля)",
                     "22-06", "22-07"),
    "leo": Zodiac("Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа)",
                  "23-07", "21-08"),
    "virgo": Zodiac("Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября)",
                    "22-08", "23-09"),
    "libra": Zodiac("Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября)",
                    "24-09", "23-10"),
    "scorpio": Zodiac("Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября)",
                      "24-10", "22-11"),
    "sagittarius": Zodiac("Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря)",
                          "23-11", "22-12"),
    "capricorn": Zodiac("Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января",
                        "23-12", "20-01"),
    "aquarius": Zodiac("Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля)",
                       "21-01", "19-02"),
    "pisces": Zodiac("Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта)",
                     "20-02", "20-03")
}

types_zodiac = {
    'fire': ['leo', 'sagittarius', 'aries'],
    'earth': ['taurus', 'virgo', 'capricorn'],
    'air': ['pisces', 'scorpio', 'cancer'],
    'water': ['libra', 'aquarius', 'gemini']
}


def index(request):
    zodiacs = list(zodiac_dict)
    context = {
        'zodiacs': zodiacs
    }
    return render(request, 'horoscope/index.html', context=context)


def get_info_about_sign_zodiac(request, sign_zodiac: str):
    description = zodiac_dict.get(sign_zodiac).description
    data = {
        'description_zodiac': description,
        'sign': sign_zodiac
    }
    return render(request, 'horoscope/info_zodiac.html', context=data)


def get_info_about_sign_zodiac_by_number(request, sign_zodiac: int):
    zodiacs = list(zodiac_dict)
    if sign_zodiac > len(zodiacs):
        return HttpResponseNotFound(f'Unknown sign zodiac - {sign_zodiac}')
    name_zodiac = zodiacs[sign_zodiac - 1]
    redirect_url = reverse('horoscope_name', args=(name_zodiac,))
    return HttpResponseRedirect(redirect_url)


def get_types_zodiac(request):
    types = list(types_zodiac)
    li_type_elements = ''
    for type_zodiac in types:
        redirect_path = reverse('horoscope_type')
        li_type_elements += f'<li><a href={redirect_path}{type_zodiac}> {type_zodiac.title()} </a></li>'
    response = f"""
    <ul>
        {li_type_elements}
    </ul>
    """
    return HttpResponse(response)


def get_zodiacs_by_type(request, type_zodiacs: str):
    signs = types_zodiac[type_zodiacs]
    li_sign_elements = ''
    for sign in signs:
        redirect_path = reverse('horoscope_name', args=(sign,))
        li_sign_elements += f'<li><a href={redirect_path}> {sign.title()} </a></li>'
    response = f"""
        <ul>
            {li_sign_elements}
        </ul>
        """
    return HttpResponse(response)


def get_info_about_sign_zodiac_by_date(request, month: int, day: int):
    try:
        dt(dt.today().year, month, day)
    except ValueError as exc:
        return HttpResponse(str(exc).capitalize())
    inp_date = f'{str(day).zfill(2)}-{str(month).zfill(2)}'
    for descr, s_d, e_d in zodiac_dict.values():
        if dt.strptime(s_d, '%d-%m') <= dt.strptime(inp_date, '%d-%m') <= dt.strptime(e_d, '%d-%m'):
            return HttpResponse(descr)
        continue
