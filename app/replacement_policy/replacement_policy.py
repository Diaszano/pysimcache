from typing import List, Any
from abc import ABC, abstractmethod


class ReplacementPolicy(ABC):
    """
    Classe base abstrata para políticas de substituição em sistemas de cache.

    Esta classe define a interface para diferentes políticas de substituição, como
    FIFO, LRU, e outras.
    """

    @staticmethod
    @abstractmethod
    def add(block: List[Any], new: Any) -> List[Any]:
        """
        Método abstrato que deve ser implementado para definir a política de substituição.

        O método deve adicionar um novo item ao bloco de cache, possivelmente substituindo
        um item existente, de acordo com a política de substituição específica.

        Parâmetros:
        -----------
        block : List[Any]
            A lista atual de itens no bloco de cache.
        new : Any
            O novo item a ser adicionado ao bloco de cache.

        Retorna:
        --------
        List[Any]
            A lista atualizada de itens no bloco de cache após a adição do novo item.
        """
        ...
