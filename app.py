from flask import Flask, render_template, request, url_for, redirect
from jinja2 import Environment, FileSystemLoader


app = Flask(__name__)

env = Environment(loader=FileSystemLoader("templates"))
env.globals["enumerate"] = enumerate


pessoas = []


@app.route('/')
def hello_world():
    return render_template('index.html', pessoas=enumerate(pessoas))


@app.route('/add-pessoa', methods=['POST'])
def add_pessoa():
    pessoa = {
        'nome': request.form['nome'],
        'celular': request.form['celular'],
        'instagram': request.form['instagram']
    }

    pessoas.append(pessoa)

    return redirect(url_for('hello_world'))


@app.route('/remove-pessoa/<int:pessoa>', methods=['POST'])
def remove_pessoa(pessoa):
    del(pessoas[pessoa])

    return redirect(url_for('hello_world'))
