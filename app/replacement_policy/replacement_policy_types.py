from enum import Enum


class ReplacementPolicyType(str, Enum):
    """
    Enumeração que define os tipos de políticas de substituição para caches.

    Esta classe enumera diferentes políticas de substituição usadas em sistemas
    de cache para decidir qual item deve ser removido quando o cache está cheio.

    Políticas de Substituição:
    --------------------------
    - random (R): Substituição aleatória. O item a ser removido é escolhido de forma aleatória.
    - fifo (F): Substituição "First In, First Out". O item adicionado primeiro é o primeiro a ser removido.
    - lru (L): Substituição "Least Recently Used". O item menos recentemente utilizado é removido primeiro.

    Atributos:
    ----------
    random: str
        Representa a política de substituição aleatória, com valor "R".
    fifo: str
        Representa a política de substituição FIFO, com valor "F".
    lru: str
        Representa a política de substituição LRU, com valor "L".
    """

    random = "R"
    fifo = "F"
    lru = "L"
