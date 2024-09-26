from abc import ABCMeta, abstractmethod

from app.cache import Block


class ReplacementPolicy(metaclass=ABCMeta):
	"""Classe abstrata que define a interface para políticas de substituição de cache.

	Todas as classes que implementam uma política de substituição específica
	(por exemplo, LRU, FIFO, Random) devem herdar de `ReplacementPolicy` e
	implementar o método abstrato `add`. O método `add` é responsável por
	definir como os blocos são gerenciados quando adicionados a um conjunto.
	"""  # noqa: E501

	@staticmethod
	@abstractmethod
	def add(blocks: list[Block], block: Block) -> list[Block]:
		"""Método abstrato que deve ser implementado por subclasses para definir a lógica de substituição.

		Args:
			blocks (list[Block]): A lista de blocos atuais.
			block (Block): O novo bloco a ser adicionado ao conjunto.

		Returns:
			list[Block]: O conjunto após a aplicação da política de substituição.
		"""  # noqa: E501
		...
