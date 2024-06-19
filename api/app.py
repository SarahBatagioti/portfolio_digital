from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sobreMim')
def sobreMim():
    return render_template('sobreMim.html')

@app.route('/projetos')
def projetos():
    projetos_lista = [
        {
            'titulo': 'Smart Farm',
            'descricao': 'Painel de visualização que permite o monitoramento constante de uma estufa através de gráficos e automatização do processo de coleta e armazenamento de dados',
            'tecnologias': ['HTML', 'CSS', 'Python'],
            'imagem': 'inicioSmartFarm.png',
            'link': 'https://github.com/andresalerno/projeto_api'
        },
        {
            'titulo': 'IZZIE - Bengala Inteligente',
            'descricao': 'Ferramenta inovadora e eficaz que promove a mobilidade independente, segurança e autonomia de crianças portadoras de cegueira em diferentes ambientes internos, visando facilitar a exploração do espaço, garantir a detecção de obstáculos e oferecer auxilio auditivo.',
            'tecnologias': ['HTML', 'CSS', 'Arduino'],
            'imagem': 'IZZIE.jpg',
            'link': 'https://www.canva.com/design/DAFvGaB8krU/3PXvDf3c4hWy9fc9CZKM_A/edit?utm_content=DAFvGaB8krU&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton'
        }
    ]
    return render_template('projetos.html', projetos=projetos_lista)

if __name__ == '__main__':
    app.run(debug=True)
