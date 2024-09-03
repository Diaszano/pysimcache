from abc import ABC, abstractmethod


class ReplacementPolicy(ABC):
	"""Classe abstrata que define a interface para políticas de substituição de
	cache.

	Todas as classes que implementam uma política de substituição específica
	(por exemplo, LRU, FIFO, Random) devem herdar de `ReplacementPolicy` e
	implementar o método abstrato `add`. O método `add` é responsável por
	definir como os elementos são gerenciados quando adicionados a uma lista.
	"""

	@staticmethod
	@abstractmethod
	def add(block: list[any], new: any) -> list[any]:
		"""Método abstrato que deve ser implementado por subclasses para definir a lógica de substituição.

		Args:
		----
			block (list[any]): A lista de elementos atuais (blocos de cache ou memória).
			new (any): O novo elemento a ser adicionado à lista.

		Returns:
		-------
			list[any]: A lista após a aplicação da política de substituição.

		"""  # noqa: E501
		...
