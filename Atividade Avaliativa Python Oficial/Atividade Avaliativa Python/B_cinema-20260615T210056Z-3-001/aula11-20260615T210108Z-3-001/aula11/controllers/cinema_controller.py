from flask import Blueprint, redirect, render_template, request, url_for
from datetime import datetime  # Importante para converter a data do formulário

from models import Filme, Sala, Sessao, db

# Blueprint = módulo de rotas do cinema (registrar no app.py com register_blueprint)
cinema_bp = Blueprint("cinema", __name__, url_prefix="/cinema")


@cinema_bp.route("/")
def index():
    # TODO ALUNO: sessoes = Sessao.listar_com_detalhes()
    sessoes = Sessao.listar_com_detalhes()
    return render_template("cinema/lista_sessoes.html", sessoes=sessoes)


@cinema_bp.route("/sessao/cadastrar", methods=["GET", "POST"])
def cadastrar_sessao():
    filmes = Filme.listar()
    salas = Sala.listar()

    if request.method == "POST":
        # TODO ALUNO: criar Sessao com filme_id, sala_id, data_hora, preco
        filme_id = request.form.get("filme_id")
        sala_id = request.form.get("sala_id")
        
        # O HTML envia a data como texto, precisamos converter para um objeto datetime do Python
        data_hora_str = request.form.get("data_hora")
        data_hora = datetime.strptime(data_hora_str, "%Y-%m-%dT%H:%M")
        
        preco = float(request.form.get("preco"))

        # Cria a nova sessão com os dados recebidos
        nova_sessao = Sessao(
            filme_id=filme_id,
            sala_id=sala_id,
            data_hora=data_hora,
            preco=preco
        )

        # Salva a nova sessão no banco de dados
        db.session.add(nova_sessao)
        db.session.commit()

        # Redireciona o usuário para a página inicial do cinema (lista de sessões)
        return redirect(url_for("cinema.index"))

    return render_template(
        "cinema/formulario_sessao.html",
        filmes=filmes,
        salas=salas,
    )