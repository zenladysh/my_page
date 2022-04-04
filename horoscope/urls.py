from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='horoscope_index'),
    path('type/', views.get_types_zodiac, name='horoscope_type'),
    path('type/<str:type_zodiacs>', views.get_zodiacs_by_type),
    path('<int:month>/<int:day>/', views.get_info_about_sign_zodiac_by_date),
    path('<int:sign_zodiac>/', views.get_info_about_sign_zodiac_by_number),
    path('<str:sign_zodiac>/', views.get_info_about_sign_zodiac, name='horoscope_name'),
]
