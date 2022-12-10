from django.urls import path

from . import views


urlpatterns = [
    # Главная страница
    path('', views.index),
    # Список постов
    path('group/', views.group_posts),
    path('group/<slug:slug>/', views.group_posts_detail),
] 