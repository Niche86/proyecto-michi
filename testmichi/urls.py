from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('procesar/', views.ProcesarView.as_view(), name='procesar'),
    path('resultado/<int:gato_id>/', views.ResultadoView.as_view(), name='resultado'),
]
