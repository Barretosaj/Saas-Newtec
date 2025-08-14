import os
from flask import Flask, render_template
from functions.remover_fundo import remover_fundo_bp
from functions.remover_bordas import remover_bordas_bp
from functions.contar_paginas import contar_paginas_bp
from functions.abnt import abnt_bp
from functions.tradutor import tradutor_bp
from functions.melhorar_imagem import melhorar_imagem_bp
from googletrans import LANGUAGES

app = Flask(__name__)
app.secret_key = "uma_senha_secreta_qualquer"
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'pdf', 'docx', 'txt', 'png', 'jpg', 'jpeg'}
app.static_folder = 'static'

# Registrar blueprints
app.register_blueprint(remover_fundo_bp)
app.register_blueprint(remover_bordas_bp, url_prefix="/remover-bordas")
app.register_blueprint(contar_paginas_bp, url_prefix="/contar-paginas")
app.register_blueprint(abnt_bp, url_prefix="/abnt")
app.register_blueprint(tradutor_bp, url_prefix="/tradutor")
app.register_blueprint(melhorar_imagem_bp)

# Criar pasta de uploads se não existir
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/resumo')
def resumo():
    return '<h1>Resumo de Texto</h1>'

@app.route('/pdf2word')
def pdf2word():
    return '<h1>Transformar PDF em Word</h1>'

@app.route('/transcrever-video')
def transcrever_video():
    return '<h1>Transcrever vídeo do YouTube</h1>'

@app.route('/mesclar-pdf')
def mesclar_pdf():
    return '<h1>Mesclar PDFs</h1>'

if __name__ == '__main__':
    app.run(debug=True)
