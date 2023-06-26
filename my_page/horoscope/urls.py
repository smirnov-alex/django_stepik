from django.urls import path
from . import views

urlpatterns = [
    path('type', views.types_page, name='types_page'),
    path('type/<str:type_sign>', views.type_info, name='type_info'),
    path('<int:month>/<int:day>', views.get_info_by_date, name='info_by_date'),
    path('<int:sign_zodiac>', views.get_info_about_zodiac_sign_by_number),
    path('<str:sign_zodiac>', views.get_info_about_zodiac_sign, name='horoscope_name'),
    path('', views.index, name='index'),
]
