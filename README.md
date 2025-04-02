# **CSI606-2024-02 - Trabalho Final**

## *Discente: Pedro Henrique Nunes de Assis*

<!-- Descrever um resumo sobre o trabalho. -->

### Resumo
  O trabalho prático desenvolvido para a disciplina CSI606 tem como foco manter um local anotação e consulta de como executar exercícios na academia. Possui um sistema de login para possíbilitar o uso de múltiplos
  usuário e página de consulta, anotação e controle dos exercícios. As ferramentas utilizadas para desenvolvimento foram: Python, Flask, Virtualenv, SQLAlchemy, HTML/CSS e JavaScript.
<!-- Apresentar o tema. -->
### 1. Tema

  O trabalho final tem como tema o desenvolvimento de hábitos de exercícios e incetivo à pratica dos mesmos. Com uma interface amigável é possível visualizar excercícios e adicionar registros do treinamento e também detalhes dos excercícios realizados. Como repetições, pesos e séries. Com o auxilio de acompanhamento profissional seria possível a utilização das informações do aplicativo para desenvolvimento de novas fichas, assim complementando as informações de perifl do usuário e possibilitando uma abordagem ainda mais direcionada com base no desenvolvimento. 

<!-- Descrever e limitar o escopo da aplicação. -->
### 2. Funcionalidades implementadas
  Este projeto terá as seguintes funcionalidades:
  - **Sistema de login, cadastro e recuperação de senha**:  Permite a criação de usuários, recuperação de senha, login/log off da aplicação;
  - **Visualização e edição de fichas, cadastro e edição de execução de exercícios**: Se trata da funcionalidade CORE do sistema, permite a adição de dias onde treinos foram executados, e adição de exercicíos, assim como a edição e exclusão de qualquer um desses registros;
  - **Dashboards personalizados**: Permite a visualização de dashboards de frequência e progressão de carga com base nos registros do usuário;
  - **Visualização, adição e exclusão de vídeos**: Permite a visualização de vídeos informativos sobre a maneira correta de se executar o exercicío.
<!-- Apresentar restrições de funcionalidades e de escopo. -->
### 3. Funcionalidades previstas e não implementadas

  Fichas de treinamento fixas, eram uma ideia de implementação prevista porém optei por um sistema mais flexível. Acredito que permitir o usuário realizar o preenchimento de forma customizada seja mais interessante, devido a grande variação de exercicíos que podem ser realizados.
  
<!-- Construir alguns protótipos para a aplicação, disponibilizá-los no Github e descrever o que foi considerado. //-->
### 4. Protótipo
1. Login - *login/login.html*
1. Signup - *login/signup.html*
1. Recovery - *login/recovery.html*
1. Dashboards - *dashboards/grafico.html*
1. Página de novo treino - *treino/novoTreino.html*
1. Listagem dos treinos - *treino/lista.html*
1. Edição dos treinos - *treino/atualizarTreino.html.html*
1. Lista dos excercícios de cada treino - *treino/listarTreino.html*
1. Edição de excercícios - *treino/atualizarAtividadesTreino.html*
1. Vídeos exemplo dos excercícios - *videos/videos.html*
1. Upload de novos vídeos - *videos/upload.html*

Todos podem ser encontrado em TP/templates.

### 5. Instruções para instalação e execução
1. Instale Python;
1. Na sua IDE de preferência abra o projeto;
1. Instale o pip com o seguinte comando: py get-pip.py;
1. Com o pip instalado, use os comandos:
    1. pip install Flask;
    1. pip install Flask-SQLAlchemy;
    1. pip install virtualenv;
    1. pip install flask_login;
1. Execute o app.py;
1. Pronto, já é possível acessar o software;


<!-- Descrever o que deve ser feito para instalar (ou baixar) a aplicação, o que precisa ser configurando (parâmetros, banco de dados e afins) e como executá-la. -->    

 
