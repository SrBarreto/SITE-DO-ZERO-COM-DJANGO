from django.shortcuts import render, redirect
from .models import Imagem, Projeto
from .forms import ImagemForm, ProjetoForm

def index(request):
    return render(request, 'core/index.html')

def sobre(request):
    return render(request, 'core/sobre.html')

def ver_imagens(request):
    imagens = Imagem.objects.all()
    return render(request, 'core/ver_imagens.html', {'imagens': imagens})

def upload_imagem(request):
    if request.method == 'POST':
        form = ImagemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ver_imagens')
    else:
        form = ImagemForm()
    return render(request, 'core/upload.html', {'form': form})

def projetos(request):
    projetos = Projeto.objects.all()
    return render(request, 'core/projetos.html', {'projetos': projetos})

def adicionar_projeto(request):
    if request.method == 'POST':
        form = ProjetoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projetos')
    else:
        form = ProjetoForm()
    return render(request, 'core/adicionar_projeto.html', {'form': form})