from flask import Blueprint, render_template

# 1. Mudamos a importação para os modelos do seu cenário (Cinema)
from models import Filme, Sala, Sessao

# Blueprint da home — sem url_prefix, então "/" é a raiz do site
dashboard_bp = Blueprint("dashboard", __name__)


@dashboard_bp.route("/")
def index():
    # 2. Mudamos as variáveis e as consultas para refletirem o Cinema
    return render_template(
        "index.html",
        total_filmes=Filme.query.count(),
        total_salas=Sala.query.count(),
        total_sessoes=Sessao.query.count(),
    )