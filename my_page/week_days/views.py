from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse
from django.shortcuts import render


weekdays = {
        'monday': 'пресс качат',
        'tuesday': 'Т) бегит',
        'wednesday': 'турник',
        'thursday ': 'анжуманя',
        'friday': 'пресс качат',
        'saturday': 'анжуманя',
        'sunday': 'ничего не делат',
    }


def greeting(request):
    return render(request, 'week_days/greeting.html')

def get_plan_on_weekday(request, weekday):
    if weekday.lower() in weekdays:
        return HttpResponse(weekdays[weekday.lower()])
    return HttpResponseNotFound(f'Неизвестный день недели: {weekday}')


def get_num_of_weekday(request, weekday: int):
    weekdays_list = list(weekdays)
    if weekday > len(weekdays_list):
        return HttpResponse(f'Неверный номер дня - {weekday}')
    name_weekday = weekdays_list[weekday - 1]
    return redirect(reverse('weekday_name', args=[name_weekday]))
