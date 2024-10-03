from typing import Type

from app.replacement_policy.random_replacement_policy import ReplacementPolicy

from .cache_block import Block

Policy = Type[ReplacementPolicy]


class Set:
	"""
	Representa um conjunto de blocos da cache.
	"""

	def __init__(self: 'Set', assoc: int, policy: Policy) -> None:
		"""
		Inicializa o conjunto de blocos.

		Args:
			assoc (int): Número associativo do conjunto.
			policy (Type[ReplacementPolicy]): Política de substituição a ser utilizada.

		Returns:
			None
		"""  # noqa: E501
		self.__assoc = assoc
		self.__policy = policy
		self.__blocks = [Block() for _ in range(self.__assoc)]

	def get_blocks(self: 'Set') -> list[Block]:
		"""
		Retorna os blocos associados ao conjunto.

		Returns:
			list[Block]: Lista de blocos associadas.
		"""
		return self.__blocks

	def add_block(self: 'Set', block: Block) -> None:
		"""
		Adiciona um novo bloco ao conjunto, substituindo outros se necessário.

		Args:
			block (Block): O bloco a ser adicionado.

		Returns:
			None
		"""
		self.__blocks = self.__policy.add(blocks=self.__blocks, block=block)

	def __len__(self: 'Set') -> int:
		"""
		Retorna o número de blocos no conjunto.

		Returns:
			int: Número de blocos no conjunto
		"""
		return len(self.__blocks)

	def __repr__(self: 'Set') -> str:
		"""
		Retorna uma representação string da instância do conjunto para fins de depuração.

		Returns:
			str: Representação string da instância para fins de depuração.
		"""  # noqa: E501
		return repr(self.__blocks)

	def __str__(self: 'Set') -> str:
		"""
		Retorna uma representação string da instância do conjunto.

		Returns:
			str: Representação string da instância.
		"""
		return str(self.__blocks)