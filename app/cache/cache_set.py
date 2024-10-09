from app.replacement_policy import ReplacementPolicy

from .cache_block import Block

Policy = type[ReplacementPolicy]


class Set:
	"""
	Representa um conjunto de blocos da cache.
	"""

	def __init__(self: 'Set', assoc: int, policy: Policy) -> None:
		"""
		Inicializa o conjunto de blocos.

		:param assoc: Número associativo do conjunto.
		:param policy: Política de substituição a ser utilizada.
		"""
		self.__assoc = assoc
		self.__blocks = [Block() for _ in range(self.__assoc)]
		self.__policy = policy

	def get_blocks(self: 'Set') -> list[Block]:
		"""
		Retorna os blocos associados ao conjunto.

		:return: Lista de blocos associadas.
		"""
		return self.__blocks

	def add_block(self: 'Set', block: Block) -> None:
		"""
		Adiciona um novo bloco ao conjunto, substituindo outros se necessário.

		:param block: O bloco a ser adicionado.
		"""
		self.__blocks = self.__policy.add(blocks=self.__blocks, block=block)

	def __len__(self: 'Set') -> int:
		"""
		Retorna o número de blocos no conjunto.

		:return: Número de blocos no conjunto
		"""
		return len(self.__blocks)

	def __repr__(self: 'Set') -> str:
		"""
		Retorna uma representação string da instância do conjunto para fins de depuração.

		:return: Representação string da instância para fins de depuração.
		"""  # noqa: E501
		return repr(self.__blocks)

	def __str__(self: 'Set') -> str:
		"""
		Retorna uma representação string da instância do conjunto.

		:return: Representação string da instância.
		"""
		return str(self.__blocks)
