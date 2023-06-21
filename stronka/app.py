#ZMAINY ALI
from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import numpy as np
from sympy import symbols, diff, simplify

app = Flask(__name__, template_folder='templates', static_folder='static')

def calculate_derivative(data, point):
    x = symbols('x')
    expr = simplify(data)  # Konwertowanie danych wejściowych na wyrażenie matematyczne
    derivative = diff(expr, x).evalf(subs={x: point})  # Obliczanie pochodnej w podanym punkcie
    der = diff(expr, x)
    return derivative, der


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/project')
def project():
    return render_template('project.html')

@app.route('/demonstration', methods=['GET', 'POST'])
def demonstration():
    if request.method == 'POST':
        function_data = request.form['function']
        point = float(request.form['point'])
        derivative, der = calculate_derivative(function_data, point)
        return render_template('demonstration.html', derivative=derivative, der=der)
    return render_template('demonstration.html')

@app.route('/authors')
def authors():
    return render_template('authors.html')

if __name__ == '__main__':
    app.run(debug=True)
