from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    html = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Mi primer proyecto Docker con Python</title>
        <style>
            body {
                font-family: 'Segoe UI', sans-serif;
                background: linear-gradient(120deg, #89f7fe, #66a6ff);
                color: #222;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                height: 100vh;
                margin: 0;
            }
            h1 {
                font-size: 2.5rem;
                color: #fff;
                text-shadow: 1px 1px 3px #333;
            }
            p {
                font-size: 1.2rem;
                color: #f0f0f0;
            }
            .card {
                background: rgba(255, 255, 255, 0.1);
                padding: 30px;
                border-radius: 15px;
                box-shadow: 0 4px 15px rgba(0,0,0,0.2);
                text-align: center;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>🐳 ¡Hola desde Docker y Flask!</h1>
            <p>Este sitio web está corriendo dentro de un contenedor Docker.</p>
            <p>Desarrollado con 💙 por Sofía</p>
        </div>
    </body>
    </html>
    """
    return render_template_string(html)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

