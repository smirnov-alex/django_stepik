from django.urls import path
from . import views

urlpatterns = [
    path('', views.greeting, name='greeting'),
    path('<int:weekday>/', views.get_num_of_weekday),
    path('<str:weekday>/', views.get_plan_on_weekday, name='weekday_name'),

]
