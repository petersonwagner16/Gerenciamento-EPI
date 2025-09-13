from django.shortcuts import render, redirect, get_object_or_404
from .models import Colaborador, Equipamento, Usuario, Emprestimo, NivelAcesso
from .forms import ColaboradorForm, EquipamentoForm, UsuarioForm, EmprestimoForm, LoginForm, RegistroForm
from django.contrib.auth import authenticate, login
from django.db.models import Q
from django.contrib import messages


def home(request):
    return render(request, 'base.html')



def colaboradores_lista(request):
    query = request.GET.get('q')
    if query:
        colaboradores = Colaborador.objects.filter(Q(nome__icontains=query))
    else:
        colaboradores = Colaborador.objects.all()
    return render(request, 'colaboradores_lista.html', {
        'colaboradores': colaboradores,
        'query': query
    })

def equipamentos_lista(request):
    query = request.GET.get('q')
    if query:
        equipamentos = Equipamento.objects.filter(Q(nome__icontains=query))
    else:
        equipamentos = Equipamento.objects.all()
    return render(request, 'equipamentos_lista.html', {
        'equipamentos': equipamentos,
        'query': query
    })

def usuarios_lista(request):
    query = request.GET.get('q')
    if query:
        usuarios = Usuario.objects.filter(Q(nome__icontains=query))
    else:
        usuarios = Usuario.objects.all()
    return render(request, 'usuarios_lista.html', {
        'usuarios': usuarios,
        'query': query
    })

def emprestimos_lista(request):
    query = request.GET.get('q')
    if query:
        emprestimos = Emprestimo.objects.filter(
            Q(colaborador__nome__icontains=query) | Q(equipamento__nome__icontains=query)
        )
    else:
        emprestimos = Emprestimo.objects.all()
    return render(request, 'emprestimos_lista.html', {
        'emprestimos': emprestimos,
        'query': query
    })

def colaboradores_criar(request):
    if request.method == 'POST':
        form = ColaboradorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('colaboradores_lista')
    else:
        form = ColaboradorForm()
    return render(request, 'colaboradores_form.html', {'form': form})

def equipamentos_criar(request):
    if request.method == 'POST':
        form = EquipamentoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Equipamento cadastrado com sucesso!')
            return redirect('equipamentos_criar')
        else:
            messages.error(request, 'Erro ao cadastrar equipamento. Verifique os dados.')
    else:
        form = EquipamentoForm()
    return render(request, 'equipamentos_form.html', {'form': form})

def usuarios_criar(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usuarios_lista')
    else:
        form = UsuarioForm()
    return render(request, 'usuarios_form.html', {'form': form})

def emprestimos_criar(request):
    if request.method == 'POST':
        form = EmprestimoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('emprestimos_lista')
    else:
        form = EmprestimoForm()
    return render(request, 'emprestimos_form.html', {'form': form})

def colaboradores_excluir(request, pk):
    colaborador = get_object_or_404(Colaborador, pk=pk)
    if request.method == 'POST':
        colaborador.delete()
        return redirect('colaboradores_lista')
    return render(request, 'colaboradores_excluir.html', {'colaborador': colaborador})

def equipamentos_excluir(request, pk):
    equipamento = get_object_or_404(Equipamento, pk=pk)
    if request.method == 'POST':
        equipamento.delete()
        return redirect('equipamentos_lista')
    return render(request, 'equipamentos_excluir.html', {'equipamento': equipamento})

def usuarios_excluir(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        usuario.delete()
        return redirect('usuarios_lista')
    return render(request, 'usuarios_excluir.html', {'usuario': usuario})

def emprestimos_excluir(request, pk):
    emprestimo = get_object_or_404(Emprestimo, pk=pk)
    if request.method == 'POST':
        emprestimo.delete()
        return redirect('emprestimos_lista')
    return render(request, 'emprestimos_excluir.html', {'emprestimo': emprestimo})

def colaboradores_editar(request, pk):
    colaborador = get_object_or_404(Colaborador, pk=pk)
    if request.method == 'POST':
        form = ColaboradorForm(request.POST, instance=colaborador)
        if form.is_valid():
            form.save()
            return redirect('colaboradores_lista')
    else:
        form = ColaboradorForm(instance=colaborador)
    return render(request, 'colaboradores_form.html', {'form': form})

def equipamentos_editar(request, pk):
    equipamento = get_object_or_404(Equipamento, pk=pk)
    if request.method == 'POST':
        form = EquipamentoForm(request.POST, instance=equipamento)
        if form.is_valid():
            form.save()
            return redirect('equipamentos_lista')
    else:
        form = EquipamentoForm(instance=equipamento)
    return render(request, 'equipamentos_form.html', {'form': form})

def usuarios_editar(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('usuarios_lista')
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'usuarios_form.html', {'form': form})

def emprestimos_editar(request, pk):
    emprestimo = get_object_or_404(Emprestimo, pk=pk)
    if request.method == 'POST':
        form = EmprestimoForm(request.POST, instance=emprestimo)
        if form.is_valid():
            form.save()
            return redirect('emprestimos_lista')
    else:
        form = EmprestimoForm(instance=emprestimo)
    return render(request, 'emprestimos_form.html', {'form': form})

def entrar_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            user = authenticate(request, username=email, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'Email ou senha incorretos.')
    else:
        form = LoginForm()
    return render(request, 'entrar.html', {'form': form})

def criar_conta_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST) 
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.set_password(form.cleaned_data['senha1'])
            
            try:
                nivel_usuario = NivelAcesso.objects.get(nome='Usuario')
            except NivelAcesso.DoesNotExist:
                nivel_usuario = NivelAcesso.objects.create(nome='Usuario')
            
            usuario.nivel_acesso = nivel_usuario
            usuario.save()
            return redirect('entrar') 
    else:
        form = RegistroForm()
    return render(request, 'criar_conta.html', {'form': form})