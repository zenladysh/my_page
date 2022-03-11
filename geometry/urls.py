from django.urls import path
from geometry import views

urlpatterns = [
    path('rectangle/<int:width>/<int:height>', views.get_rectangle_area),
    path('square/<int:width>', views.get_square_area),
    path('circle/<int:radius>', views.get_circle_area),
    path('<str:get_rectangle_area>/<int:width>/<int:height>', views.get_figure_area),
    path('<str:get_square_area>/<int:width>', views.get_figure_area),
    path('<str:get_circle_area>/<int:radius>', views.get_figure_area)
]