from django.urls import path
from . import views

urlpatterns = [
    # Главная страница
    path('', views.index),
    path('urls/', views.show_all_shorted_urls),
    path('short/<str:param>',  views.get_shorted_url),
]
