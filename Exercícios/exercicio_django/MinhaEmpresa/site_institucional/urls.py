from django.urls import path
from . import views

urlpatterns = [
  path('home/', views.home, name='home'),
  path('servicos/', views.servicos, name='servicos'),
  path('fale_conosco/', views.fale_conosco, name='fale_conosco'),
]