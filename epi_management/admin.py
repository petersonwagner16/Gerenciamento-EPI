# No seu arquivo admin.py

# ... (seus outros imports)
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import StatusEquipamento, StatusEmprestimo, NivelAcesso, Colaborador, Equipamento, Usuario, Emprestimo

# ... (seus outros registros de modelos)
admin.site.register(StatusEquipamento)
admin.site.register(StatusEmprestimo)
admin.site.register(NivelAcesso)
admin.site.register(Colaborador)
admin.site.register(Equipamento)
admin.site.register(Emprestimo)


class UsuarioAdmin(UserAdmin):

    list_display = ('email', 'nome', 'nivel_acesso')
    search_fields = ('email', 'nome')
    ordering = ('email',)


    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Informações Pessoais', {'fields': ('nome', 'nivel_acesso')}),
    )


    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'nome', 'nivel_acesso', 'password'),
        }),
    )
    

    filter_horizontal = ()
    list_filter = ()


admin.site.register(Usuario, UsuarioAdmin)