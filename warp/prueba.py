from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def index():
    var1 = os.getenv('VAR1', 'ENCONTRADO')
    var2 = os.getenv('VAR2', 'VALOR 2 NO ENCONTRADO')

    return f"""
    <html>
        <head><title>Variables de Entorno</title></head>
        <body>
            <h1>Variables desde Dockerr</h1>
            <p><strong>VAR1:</strong> {var1}</p>
            <p><strong>VAR2:</strong> {var2}</p>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)  # 👈 esto activa live reload