from django.shortcuts import render
from .models import Usuario


def home(request):
    return render(request, 'home.html')

def usuarios(request):
    if request.method == 'POST':
        # Salvar os dados da tela para o banco de dados.
        novo_usuario = Usuario()  # Aqui é instanciado um novo objeto da classe Usuario
        novo_usuario.nome = request.POST.get('nome')
        novo_usuario.idade = request.POST.get('idade')
        novo_usuario.save()

    # Exibir todos os usuários já cadastrados em uma nova página
    usuarios = {
        'usuarios': Usuario.objects.all()  # Aqui é recuperada a lista de todos os usuários cadastrados
    }

    # Retornar os dados para a página de listagem de usuários
    return render(request, 'usuarios.html', usuarios)
    
