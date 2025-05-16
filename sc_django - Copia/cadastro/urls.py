from django.urls import path
from . import views

urlpatterns = [
    path('', views.formulario_view, name='formulario'),   # Mostra e processa o formulário
    path('sucesso', views.sucesso_view, name='sucesso'),   # Página de sucesso
]
