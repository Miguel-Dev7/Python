# Aqui nasce o "db" — é ele que conversa com o arquivo .db do SQLite.
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# O PONTO (.) no import = "pega da MESMA pasta models/"
from .base import db
from .filme import Filme
from .sala import Sala
from .sessao import Sessao
from .ingresso import Ingresso  # Se não for usar ingresso agora, pode deixar ou comentar

# O __all__ avisa ao Python o que deve ser exportado publicamente desta pasta
__all__ = ["db", "Filme", "Sala", "Sessao", "Ingresso"]