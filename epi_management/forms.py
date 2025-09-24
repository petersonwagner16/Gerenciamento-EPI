from django import forms
from .models import Colaborador, Equipamento, Usuario, Emprestimo, StatusEquipamento, StatusEmprestimo, NivelAcesso
from django.core.exceptions import ValidationError
from datetime import date

class ColaboradorForm(forms.ModelForm):
    class Meta:
        model = Colaborador
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'setor': forms.TextInput(attrs={'class': 'form-control'}),
            'funcao': forms.TextInput(attrs={'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control'}),
        }

class EquipamentoForm(forms.ModelForm):
    class Meta:
        model = Equipamento
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'quantidade_disponivel': forms.NumberInput(attrs={'class': 'form-control'}),
            'validade': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(EquipamentoForm, self).__init__(*args, **kwargs)
        
        
        if self.instance and self.instance.pk:
            self.fields['status'].queryset = StatusEquipamento.objects.all()
        
        else:
            self.fields['status'].queryset = StatusEquipamento.objects.filter(
                nome__in=['Emprestado', 'Fornecido', 'Em uso']
            )
class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'email', 'nivel_acesso']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'nivel_acesso': forms.Select(attrs={'class': 'form-control'}),
        }

class EmprestimoForm(forms.ModelForm):
    class Meta:
        model = Emprestimo
        fields = '__all__'
        widgets = {
            'data_emprestimo': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'data_devolucao_prevista': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'data_devolucao_efetiva': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'colaborador': forms.Select(attrs={'class': 'form-control'}),
            'equipamento': forms.Select(attrs={'class': 'form-control'}),
            'observacoes_devolucao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

   
    def __init__(self, *args, **kwargs):
        super(EmprestimoForm, self).__init__(*args, **kwargs)

    def clean_data_devolucao_prevista(self):
        data_prevista = self.cleaned_data.get('data_devolucao_prevista')
        if data_prevista and data_prevista <= date.today():
            raise ValidationError("A data prevista para devolução deve ser posterior à data de hoje.")
        return data_prevista


