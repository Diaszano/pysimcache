from typing import Type

from app.replacement_policy.random_replacement_policy import ReplacementPolicy
from .cache_block import Block
from ..replacement_policy import ReplacementPolicyType, LRU, FIFO, Random

Policies = ReplacementPolicyType
Policy = Type[ReplacementPolicy]

class Set:
	"""
	Representa um conjunto de blocos da cache.
	"""

	def __init__(self: 'Set', assoc: int, policy: Policies) -> None:
		"""
		Inicializa o conjunto de blocos.

		Args:
			assoc (int): Número associativo do conjunto.
			policy (Policies): Política de substituição a ser utilizada.

		Returns:
			None
		"""
		self.__assoc = assoc
		self.__blocks = [Block() for _ in range(self.__assoc)]
		self.__policy = self.create_policy(policy)  # Cria a instância da política

	@staticmethod
	def create_policy(policy_type: Policies) -> ReplacementPolicy:
		"""
		Cria uma instância da política de substituição correspondente ao tipo fornecido.

		Args:
			policy_type (Policies): Tipo da política de substituição.

		Returns:
			ReplacementPolicy: Instância da política de substituição.
		"""
		if policy_type == ReplacementPolicyType.RANDOM:
			return Random()  # Retorna uma instância de Random
		elif policy_type == ReplacementPolicyType.FIFO:
			return FIFO()  # Retorna uma instância de FIFO
		elif policy_type == ReplacementPolicyType.LRU:
			return LRU()  # Retorna uma instância de LRU
		else:
			raise ValueError("Invalid replacement policy type")

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
		"""
		return repr(self.__blocks)

	def __str__(self: 'Set') -> str:
		"""
		Retorna uma representação string da instância do conjunto.

		Returns:
			str: Representação string da instância.
		"""
		return str(self.__blocks)
