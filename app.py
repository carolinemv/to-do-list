from flask import Flask, render_template
from list import *

#Definindo o app flask
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/lista", methods=['GET'])
def lista():
    return render_template('lista.html')
