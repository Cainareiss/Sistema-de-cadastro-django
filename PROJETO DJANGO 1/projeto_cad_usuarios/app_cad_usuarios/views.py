from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest
from .models import Usuario

from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest
from .models import Usuario

def home(request):
    return render(request, 'home.html')

def usuarios(request):
    if request.method == 'POST':
        # Salvar os dados da tela para o banco de dados.
        novo_usuario = Usuario()
        novo_usuario.nome = request.POST.get('nome')
        novo_usuario.idade = request.POST.get('idade')
        novo_usuario.save()

    # Recuperar a lista de usuários cadastrados
    usuarios = Usuario.objects.all()

    # Verificar se os IDs dos usuários são válidos
    for usuario in usuarios:
        if not usuario.id:
            usuario.delete()  # Excluir usuário sem ID
            return HttpResponseBadRequest("Um ou mais usuários sem ID foram removidos.")
    
    # Passar a lista de usuários para o template
    return render(request, 'usuarios.html', {'usuarios': usuarios})

def remover_usuarios(request, id):
    if request.method == 'POST':
        usuario = Usuario.objects.get(id=id)
        usuario.delete()
        return redirect('listagem_usuarios')
    else:
        # Se o método não for POST, talvez você queira retornar um erro ou redirecionar para outra página
        return HttpResponseBadRequest("Método não permitido")
