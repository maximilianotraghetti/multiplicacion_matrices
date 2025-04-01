from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/crear', methods=['POST'])
def crear():
    filas_a = int(request.form['filas_a'])
    columnas_a = int(request.form['columnas_a'])
    filas_b = int(request.form['filas_b'])
    columnas_b = int(request.form['columnas_b'])
    
    if columnas_a != filas_b:
        return "Error: Para multiplicar, las columnas de A deben ser iguales a las filas de B."
    
    return render_template('matrices.html', filas_a=filas_a, columnas_a=columnas_a, filas_b=filas_b, columnas_b=columnas_b)

@app.route('/multiplicar', methods=['POST'])
def multiplicar():
    filas_a = int(request.form['filas_a'])
    columnas_a = int(request.form['columnas_a'])
    filas_b = int(request.form['filas_b'])
    columnas_b = int(request.form['columnas_b'])

    matriz_a = [[int(request.form[f"a_{i}_{j}"]) for j in range(columnas_a)] for i in range(filas_a)]
    matriz_b = [[int(request.form[f"b_{i}_{j}"]) for j in range(columnas_b)] for i in range(filas_b)]

    resultado = [[sum(matriz_a[i][k] * matriz_b[k][j] for k in range(columnas_a)) for j in range(columnas_b)] for i in range(filas_a)]

    return render_template('result.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
