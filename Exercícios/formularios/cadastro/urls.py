from django.urls import path
from .views import formulario

urlpatterns = [
  path('', formulario, name='formulario'),
]