from jinja2 import Environment, FileSystemLoader

# 1. Configura o Jinja para buscar templates na pasta atual
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('template.html')

# 2. Cria todos os dados solicitados na atividade
dados_da_atividade = {
    "nome": "Carlos",
    "idade": 28,
    "usuario": {"nome": "Ana", "email": "ana@email.com"},
    "alunos": ["Bruno", "Camila", "Daniel", "Eduarda"],
    "nota": 8.5
}

# 3. Junta o template com os dados (Renderização)
resultado_final = template.render(dados_da_atividade)

# 4. Salva o resultado em um novo arquivo para você visualizar no navegador
with open("resultado.html", "w", encoding="utf-8") as f:
    f.write(resultado_final)

print("Pronto! Arquivo 'resultado.html' gerado com sucesso.")
