from django.contrib import admin
from .models import Cliente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'cpf', 'rg', 'telefone', 'cidade', 'estado')
    search_fields = ('nome', 'email', 'cpf', 'rg', 'telefone', 'cidade', 'estado')