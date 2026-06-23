import os

from flask import Flask

# Cada "bp" importado é um Blueprint — um pacote de rotas (dashboard e cinema)
from controllers import blueprints_do_projeto
from models import Filme, Sala, Sessao, db  # Se usou Ingresso, adicione aqui


def criar_app():
    app = Flask(
        __name__,
        template_folder="views/templates",
        static_folder="views/static",
    )

    pasta = os.path.abspath(os.path.dirname(__file__))
    # Mudamos o banco de dados para cinema.db
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
        pasta, "cinema.db"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    # BLUEPRINT — Registro Automático:
    # Usamos a lista 'blueprints_do_projeto' que criamos no __init__.py dos controllers.
    # Isso evita ter que ficar fazendo app.register_blueprint() um por um.
    for bp in blueprints_do_projeto:
        app.register_blueprint(bp)

    # Cria as tabelas do Cinema no banco de dados se elas não existirem
    with app.app_context():
        db.create_all()

    return app


app = criar_app()

if __name__ == "__main__":
    app.run(debug=True)