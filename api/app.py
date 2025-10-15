from flask import Flask, render_template, send_file

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download_curriculum')

@app.route('/sobreMim')
def sobreMim():
    return render_template('sobreMim.html')

@app.route('/projetos')
def projetos():
    projetos_lista = [
        {
            'titulo': 'Viva Sabores',
            'descricao': 'Aplicativo de receitas culinárias que permite aos usuários explorar, salvar e compartilhar suas receitas favoritas, além de criar listas de compras personalizadas',
            'tecnologias': ['React Native', 'PostgreSQL', 'JavaScript'],
            'imagem': 'vivasabores.png',
            'link': 'https://github.com/SarahBatagioti/app-receitas',
            'categoria': 'academico'
        },
        {
            'titulo': 'Vagalume -  Raspagem de dados',
            'descricao': 'Raspagem de dados do Linkedin para coleta de dados profissionais e resumo usando LLM Ollama',
            'tecnologias': ['Python', 'Ollama'],
            'imagem': 'vagalume.png',
            'link': 'https://github.com/SarahBatagioti/bertoti-vagalume',
            'categoria': 'academico'
        },
        {
            'titulo': 'CloudStock',
            'descricao': 'Sistema de controle de estoque desenvolvida para facilitar a gestão de produtos, fornecedores e movimentações de estoque',
            'tecnologias': ['React', 'Typescript', 'MYSQL'],
            'imagem': 'cloudstock.png',
            'link': 'https://github.com/SkyFlyTeam/cloudStock',
            'categoria': 'academico'
        },
        {
            'titulo': 'Smart Farm',
            'descricao': 'Painel de visualização que permite o monitoramento constante de uma estufa através de gráficos e automatização do processo de coleta e armazenamento de dados',
            'tecnologias': ['HTML', 'CSS', 'PYTHON'],
            'imagem': 'inicioSmartFarm.png',
            'link': 'https://github.com/andresalerno/projeto_api',
            'categoria': 'academico'
        },
        {
            'titulo': 'IZZIE - Bengala Inteligente',
            'descricao': 'Ferramenta inovadora e eficaz que promove a mobilidade independente, segurança e autonomia de crianças portadoras de cegueira em diferentes ambientes internos, visando facilitar a exploração do espaço, garantir a detecção de obstáculos e oferecer auxilio auditivo.',
            'tecnologias': ['TYPESCRIPT', 'CHACKRA UI', 'ARDUINO'],
            'imagem': 'IZZIE.jpg',
            'link': 'https://github.com/SarahBatagioti/TCC-IZZIE-ARDUINO',
            'categoria': 'academico'
        },
        {
            'titulo': 'MBViagens',
            'descricao': 'Site desenvolvido para ter aprendizado sobre conexão com banco de dados, ao ter uma tela de registro de roteiros de viagem, e de utilização do docker',
            'tecnologias': ['HTML', 'CSS', 'MYSQL', 'DOCKER'],
            'imagem': 'mbviagens.png',
            'link': 'https://github.com/SarahBatagioti/Desafio3',
            'categoria': 'academico'
        },
        {
            'titulo': 'Requisições ORM',
            'descricao': 'Sistema usando requisições ORM, com disponibilidade de teste de rotas no back e front. Tem o objetivo de fazer um histórico de compras',
            'tecnologias': ['JavaScript', 'Reatc', 'MYSQL'],
            'imagem': 'rorm.png',
            'link': 'https://github.com/SarahBatagioti/requisicoesORM',
            'categoria': 'academico'
        },
        {
            'titulo': 'IA detectora de fake news',
            'descricao': 'Projeto desenvolvido na quinta edição do Technovation Summer School For Girls. O protótipo consiste em uma inteligência artificial treinada para detectar padrões comuns em informações falsas',
            'tecnologias': ['Python', 'HTML', 'JavaScript'],
            'imagem': 'iaex.png',
            'link': 'https://github.com/SarahBatagioti/IA-detectora-de-fake-news',
            'categoria': 'academico'
        },
        {
            'titulo': 'SS Passeios em Campos do Jordão',
            'descricao': 'Desenvolvido como trabalho freelance, onde junto com meu colega de trabalho fizemos um site de apresentação da loja do cliente. Colaborei com a elaboração do design do site e a estilização',
            'tecnologias': ['HTML', 'CSS', 'FIGMA'],
            'imagem': 'sspasseios.png',
            'link': 'https://github.com/SarahBatagioti/SS-PASSEIOS-EM-C.-DO-JORDAO.git',
            'categoria': 'profissional'
        },
        {
            'titulo': 'Jogo dos 7 erros com OpenCV',
            'descricao': 'Com o objetivo de no final fazer um programa para identificar erros em peças de uma indústria, durante meus estudos consegui desenvolver um jogo de sete erros, que faz a subtração de duas imagens',
            'tecnologias': ['PYHTON', 'OpenCV'],
            'imagem': 'jogo.png',
            'link': 'https://github.com/SarahBatagioti/Implementar-jogo-7-erros-em-Python.git',
            'categoria': 'profissional'
        }
    ]
    return render_template('projetos.html', projetos=projetos_lista)

if __name__ == '__main__':
    app.run(debug=True)
