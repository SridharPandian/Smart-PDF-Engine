from django.urls import path

from . import views

urlpatterns = [
    path('', views.search, name='search'),
    path('<str:word>/', views.word_detail, name='wordDetail'),
]