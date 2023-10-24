from django.urls import path
from app_metaFinanceira import views

urlpatterns = [
    # configuração das rotas
    path('', views.home, name='home'),
    path('calcular', views.calcular, name='calcular'),
]
