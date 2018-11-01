from django.contrib import admin
from .models import Fornecedor
# Register your models here.

class FornecedorAdmin(admin.ModelAdmin):
    #fields = ('nome', 'codigo', 'status', 'cnpj')
    list_filter = ('ativo', )
    list_display = ('id', 'nome', 'codigo', 'ativo', 'cnpj')
    search_fields = ('id', 'nome', 'codigo','ativo', 'cnpj')

admin.site.register(Fornecedor, FornecedorAdmin)