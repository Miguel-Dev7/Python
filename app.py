from flask import Flask

app = Flask(__name__)

# Rota principal para facilitar o teste
@app.route('/')
def home():
    return 'Acesse <a href="/decorator">/decorator</a> para ver a explicação.'

# Rota solicitada na atividade
@app.route('/decorator')
def explicar_decorator():
    texto = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Currículo de Miguel</title>
    <!-- Linha que conecta o HTML ao arquivo CSS externo -->
    <link rel="stylesheet" href="css/estilo.css">
</head>
<body>

    <!-- Informações Pessoais -->
    <h1>Miguel de Oliveira Maciel</h1>
    <p class="Miguel">Miguel</p>
    
    <p class="contato">
        📧 E-mail: migueldeoliveiramaciel07@gmail.com | 📱 Telefone: (27) 99855-6006 <br>
        🔗 LinkedIn: <a href="https://www.linkedin.com/in/miguel-de-oliveira-maciel-2b8bbb369/" target="_blank">Linkedin</a>
    </p>

    <!-- Resumo Profissional -->
    <h2>Resumo Profissional</h2>
    <p></p>

    <!-- Competências / Habilidades -->
    <h2>Habilidades</h2>
    <div class="habilidades">
        <span>HTML e CSS,</span>
        <span>MySQL,</span>
        <span>Trino,</span>
        <span>Pacote Office,</span>
        <span></span>
    </div>

    <!-- Histórico Profissional -->
    <h2>Experiência Profissional</h2>
    
    <div class="item-exp">
        <span class="periodo">2025 - 2027,</span>
        <strong>Menor Aprendiz</strong> no <span class="empresa">Banco Inter</span>
        <p></p>
    </div>

    <div class="item-exp">
        <span class="periodo"></span>
        <strong></strong> <span class="empresa"></span>
        <p></p>
    </div>

    <!-- Educação / Formação -->
    <h2>Formação Acadêmica</h2>
    
    <div class="item-exp">
        <span class="periodo">2025 - 2026</span>
        <strong>Colegio Cotemig</strong> <span class="empresa"></span>
    </div>

</body>
</html>

    """
    return texto

if __name__ == '__main__':
    app.run(debug=True)
