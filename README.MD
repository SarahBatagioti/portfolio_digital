<p align="center">
  <img src="./api/static/img/FotoSarahBatagioti.png" alt="Foto" width="20%"/>
  <img src="./api/static/img/LogoSMB.svg" alt="Foto" width="20%"/>
</p>

<h1> Portfólio digital de Sarah Montuani Batagioti </h1>

<h2> Orientador: Fabrício Galende Marques de Carvalho </h2>

<h2> 🛠️ Tecnologias utilizadas: </h2>

- Git/GitHub
- HTML
- CSS
- Bootstrap
- Markdown
- Figma (elaboração wireframe)

<h2> 🖥️ Executando a aplicação: </h2>
<h4> 1. Pesquise por "Terminal" ou "CMD" na sua barra de tarefas e abra o terminal do seu dispositivo.</h4>
<h4> 2. Clone o repositório com o comando: </h4>
  
      git clone https://github.com/SarahBatagioti/portfolio_digital.git

  <h4> 3. Acesse a pasta do projeto com o comando: </h4>
  
      cd portfolio_digital
  
<h4> 4. Abrir powershell como administrador (botão direito do mouse e selecionar "Executar como administrador)" e rodar Libere a criação apertando a letra "A" quando aparecer a mensagem de alteração da politica de execução </h4>

      Set-ExecutionPolicy –ExecutionPolicy AllSigned 

<h4> 5. Inicie um ambiente virtual para rodar o projeto: </h4>

      py -3 -m venv venv
  
<h4>  6. Execute o ambiente com os seguintes comandos: </h4>

      cd venv\Scripts
      activate

<h4 style='color: green'> Para verificar se foi iniciado, aparecerá um (venv) antes do caminho da sua pasta<h4>

<h4> 7.  Colocar as dependencias de um projeto em um arquivo de texto e instalar </h4>
      
      pip freeze > requirements.
      Pip3 install –r requirements.txt
      pip install flask
  
<h4> 8. Entrar na pasta onde está localizado a aplicação </h4>

      cd ../..
      cd api

<h4> 9. Rodar a aplicação e acessar clicando no link enquanto segura a tecla ctrl, ou <a href="http://127.0.0.1:5000"> clique aqui. </a> </h4>

      flask run

<h4> 10. Após utilizar a aplicação, volte no terminal, aperte crtl + c e digite "s" para encerrar a aplicação. </h4>
