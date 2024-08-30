"""
Módulo de inicialização do pacote.

Este módulo inicializa o pacote e define os elementos que serão exportados quando o pacote for importado.

Imports:
--------
from .file import File
    Importa a classe File do módulo file.

Variáveis:
----------
__all__
    Lista de elementos que serão exportados quando o pacote for importado.
"""

from .file import File

__all__ = ("File",)
