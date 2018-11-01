from django.contrib import admin
from .models import Empregado, Telefone, CPF, Departamento

# Register your models here.

class EmpregadoAdmin(admin.ModelAdmin):
    #fields = ('nome', 'endereco')
    list_display = ('id','nome', 'endereco', 'email')
    list_filter = ('departamento', )
    search_fields = ('id', 'nome', 'email', 'departamento__nome')

admin.site.register(Empregado, EmpregadoAdmin)
admin.site.register(Telefone)
admin.site.register(CPF)
admin.site.register(Departamento)
