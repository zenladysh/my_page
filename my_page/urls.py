from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('horoscope/', include('horoscope.urls')),
    path('todo_week/', include('week_days.urls')),
    path('calculate_geometry/', include('geometry.urls'))
]
