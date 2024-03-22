from django.urls import path
from app_cad_usuarios import views

urlpatterns = [
   # rota, view responsavel, nome de referencia
   # usuarios.com
   path('', views.home, name='home'),
   # usuarios.com/usuarios
   path('usuarios/', views.usuarios, name='listagem_usuarios'),
   # Esta rota será para remover um usuário específico, então vamos adicionar um parâmetro 'id' para diferenciá-la
   path('usuarios/remover/<int:id>/', views.remover_usuarios, name='remover_usuarios')
]
