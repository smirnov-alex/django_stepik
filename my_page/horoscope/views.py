from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from .zodiac_data import dates, zodiac_dict, zodiac_type
from django.template.loader import render_to_string


def index(request):
    zodiac_list = list(zodiac_dict)
    data = {"zodiac_list": zodiac_list}
    return render(request, 'horoscope/index.html', context=data)


def types_page(request):
    types_list = list(zodiac_type)
    li_elements = ''
    for type_item in types_list:
        redirect_path = reverse('type_info', args=(type_item,))
        li_elements += f'<li><a href="{redirect_path}">{type_item.title()}</a></li>'
    response = f'''
    <ul>
        {li_elements}
    </ul>
    '''
    return HttpResponse(response)


def type_info(request, type_sign):
    signs_list = zodiac_type.get(type_sign, None)
    li_elements = ''
    for sign_item in signs_list:
        redirect_path = reverse('horoscope_name', args=(sign_item,))
        li_elements += f'<li><a href="{redirect_path}">{sign_item.title()}</a></li>'
    response = f'''<h2>{type_sign.title()}</h2>
        <ul>
            {li_elements}
        </ul>
        '''
    return HttpResponse(response)


def get_info_about_zodiac_sign(request, sign_zodiac):
    description = zodiac_dict.get(sign_zodiac)
    data = {
        'description_zodiac': description,
        'sign': sign_zodiac,
        'zodiacs': zodiac_dict,
    }
    return render(request, 'horoscope/info_zodiac.html', context=data)


def get_info_about_zodiac_sign_by_number(request, sign_zodiac: int):
    zodiac_list = list(zodiac_dict)
    if sign_zodiac > len(zodiac_list):
        return HttpResponseNotFound(f'Неправильный порядковый номер знака зодиака: {sign_zodiac}')
    name_zodiac = zodiac_list[sign_zodiac - 1]
    return HttpResponseRedirect(reverse('horoscope_name', args=(name_zodiac,)))


def get_info_by_date(request, month, day):
    month_dict = dates.get(month, None)
    if month_dict:
        for item in month_dict.keys():
            if item[0] <= day <= item[1]:
                return HttpResponse(f'<h2>Месяц - {month}, день - {day}</h2><p>{zodiac_dict[month_dict[item]]}</p>')
        return HttpResponseNotFound(f'Неправильный номер дня ({day}) для месяца {month}')
    return HttpResponseNotFound(f'Неправильный номер месяца: {month}')
