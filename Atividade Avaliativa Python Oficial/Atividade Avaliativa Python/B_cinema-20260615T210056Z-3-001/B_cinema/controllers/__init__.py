# Esta pasta controllers/ exporta os Blueprints para o app.py registrar.
# Cada arquivo *_controller.py cria um Blueprint com nome único.
from .dashboard_controller import dashboard_bp
from .cinema_controller import cinema_bp

# Criamos uma lista com os blueprints ativos para facilitar o registro no app.py
blueprints_do_projeto = [dashboard_bp, cinema_bp]

__all__ = ["dashboard_bp", "cinema_bp", "blueprints_do_projeto"]