from flask import Flask, render_template, send_file
from fpdf import FPDF

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def generate_pdf():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Currículo de Sarah Batagioti", ln=True, align="C")
    pdf.cell(200, 10, txt="Desenvolvedora Fullstack Júnior", ln=True, align="C")
    pdf.output("static/pdf/csmb.pdf")

@app.route('/download_curriculum')
def download_curriculum():
    # Gere o PDF antes de enviar
    generate_pdf()
    # Diretório onde o PDF está localizado
    pdf_path = "static/pdf/csmb.pdf"
    return send_file(pdf_path, as_attachment=True)

@app.route('/sobreMim')
def sobreMim():
    return render_template('sobreMim.html')

@app.route('/projetos')
def projetos():
    projetos_lista = [
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
            'link': 'https://www.canva.com/design/DAFvGaB8krU/3PXvDf3c4hWy9fc9CZKM_A/edit?utm_content=DAFvGaB8krU&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton',
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
            'tecnologias': ['PYHTON'],
            'imagem': 'jogo.png',
            'link': 'https://github.com/SarahBatagioti/Implementar-jogo-7-erros-em-Python.git',
            'categoria': 'profissional'
        }
    ]
    return render_template('projetos.html', projetos=projetos_lista)

if __name__ == '__main__':
    app.run(debug=True)
