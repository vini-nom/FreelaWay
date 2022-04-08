# FreelaWay *PyStackWeek*

O FreelaWay é um projeto desenvolvido na PyStackWeek 3.0, que funciona como um app para divulgar trabalhos de edição de vídeo e design de uma empresa.
O projeto foi desenvolvido com:

- Python
- Pillow
- Django
- Bootstrap
- CSS
- HTML

## Intalação do Django e Pillow

- ``pip install django``
- ``pip install pillow``

# Rotas

__freelaway/urls__

aqui são definidos os caminhos principais e rotas que serão incluidas, que estão relacionada as pastas **Autenticacao** e **jobs**

- **Admin** (caminho da para área do administrador do Django)
- **Auth** (caminho da pasta Autenticacao)
- **jobs** (caminho da pasta Jobs)

__Autenticacao/urls__

aqui são definidos os caminhos de relativos ao **Auth**, que são: 

- **auth/cadastro** (caminho para a área de cadastro)
- **auth/login** (caminho para a área de login) 
- **auth/sair** (caminho para o logout) 
- **auth/password_reset** (caminho para a recuperação de senha) 
- **auth/password_reset_done** (caminho de confirmação de envio de e-mail) 
- **auth/reset/<uidb64>/<token>** (caminho para a confirmação da nova senha com token) 
- **auth/password_reset_complete** (caminho para a confirmação da alteração da senha) 
  
__jobs/urls__

aqui são definidos os caminhos de relativos ao **jobs**, que são:
  
- **jobs/encontrar_jobs** (caminho para a tela principal do usuário onde aceita e pesquisa por trabalhos)
- **jobs/perfil** (caminho para a tela de perfil onde o usuário pode ver o status dos seus trabalhos e alterar suas informações)
- **jobs/aceitar_job** (caminho para a ocupação de um trabalho para um usuário)
- **jobs/envia_projeto** (caminho para enviar um projeto completo)
  
# Funcionalidade

1. O FreelaWay exige credenciais de acesso com um sistema de login que usa o nome do usuário e senha.
2. 

