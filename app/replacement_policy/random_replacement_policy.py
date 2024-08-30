from typing import List, Any
from random import randint
from .replacement_policy import ReplacementPolicy

class RandomReplacementPolicy(ReplacementPolicy):
    """
    Implementação da política de substituição aleatória para caches.

    Esta classe implementa a política de substituição onde um item é escolhido aleatoriamente
    e substituído por um novo item. Herda da classe abstrata `ReplacementPolicy` e fornece
    uma implementação concreta do método `add`.

    Métodos:
    --------
    add(block: List[Any], new: Any) -> List[Any]
        Substitui um item aleatório no bloco de cache com um novo item.

    Parâmetros:
    -----------
    block : List[Any]
        A lista atual de itens no bloco de cache. Pode conter qualquer tipo de objeto.
    new : Any
        O novo item a ser adicionado ao bloco de cache.

    Retorna:
    --------
    List[Any]
        A lista de itens no bloco de cache após a substituição do item aleatório
        pelo novo item.
    """

    @staticmethod
    def add(block: List[Any], new: Any) -> List[Any]:
        """
        Substitui um item aleatório no bloco de cache com o novo item fornecido.

        O método escolhe um índice aleatório no bloco de cache e substitui o
        item nesse índice
        pelo novo item.

        Parâmetros:
        -----------
        block : List[Any]
            A lista atual de itens no bloco de cache.
        new : Any
            O novo item a ser adicionado ao bloco de cache.

        Retorna:
        --------
        List[Any]
            A lista atualizada de itens no bloco de cache após a substituição.
        """
        length = len(block)

        block[randint(a=0, b=length - 1)] = new

        return block
