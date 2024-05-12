from flask import Flask, render_template # type: ignore

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/sobreMim')
def sobreMim():
    return render_template('sobreMim.html')

@app.route('/projetos')
def projetos():
    return render_template('projetos.html')

if __name__ == '__main__':
    app.run(debug=True)