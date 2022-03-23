from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('type/', views.get_types_zodiac, name='horoscope_type'),
    path('type/<str:type_zodiacs>', views.get_zodiacs_by_type),
    path('<int:sign_zodiac>/', views.get_info_about_sign_zodiac_by_number),
    path('<str:sign_zodiac>/', views.get_info_about_sign_zodiac, name='horoscope_name'),
    path('<int:date_month>/<int:date_day>/', views.get_info_about_sign_zodiac_by_date),
]
