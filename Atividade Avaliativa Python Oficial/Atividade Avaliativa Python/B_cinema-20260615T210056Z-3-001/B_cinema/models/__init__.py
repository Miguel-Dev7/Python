from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .base import db
from .filme import Filme
from .sala import Sala
from .sessao import Sessao
from .ingresso import Ingresso 

# 2. ADICIONE NA LISTA __all__ TAMBÉM
__all__ = ["db", "Filme", "Sala", "Sessao", "Ingresso", "Cliente", "Pedido"]