from logging import getLogger
from math import log2

from app.replacement_policy import ReplacementPolicy

from .cache_block import Block
from .cache_set import Set

Policy = type[ReplacementPolicy]


class Mapping:
	"""
	Classe responsável por realizar o mapeamento de endereços de memória
	em um cache com múltiplos conjuntos (sets) e associatividade.

	A classe gerencia os acertos (hits) e diferentes tipos de erros de cache (misses)
	durante a simulação do mapeamento de endereços.
	"""  # noqa: E501

	__logger = getLogger(name=__name__)

	def __init__(
		self: 'Mapping',
		nsets: int,
		bsize: int,
		assoc: int,
		policy: Policy,
	) -> None:
		"""
		Inicializa um objeto CacheMapping.

		:param nsets: Número de conjuntos (sets) no cache.
		:param bsize: Tamanho do bloco de cache em bytes.
		:param assoc: Grau de associatividade do cache.
		:param policy: Classe de política de substituição utilizada no cache.
		"""
		self.hits = 0
		self.misses = 0
		self.miss_compulsory = 0
		self.miss_capacity = 0
		self.miss_conflict = 0
		self.sets = [Set(assoc, policy) for _ in range(nsets)]
		self.nbits_offset = int(log2(bsize))
		self.nbits_index = int(log2(nsets))
		self.nbits_tag = 32 - self.nbits_offset - self.nbits_index

	def mapping(
		self: 'Mapping', memory_addresses: list[int]
	) -> tuple[int, int, int, int, int]:
		"""
		Realiza o mapeamento de uma lista de endereços de memória no cache.

		:param memory_addresses: Lista de endereços de memória a serem mapeados.
		:return: Resultado do mapeamento da cache.
		"""
		self.__logger.info(
			'Iniciando o mapeamento de %s endereços de memória',
			len(memory_addresses),
		)

		for address in memory_addresses:
			tag = address >> (self.nbits_offset + self.nbits_index)
			idx = (address >> self.nbits_offset) & (2**self.nbits_index - 1)
			self.__logger.debug(
				'Endereço %s -> Tag: %s, Índice: %s', address, tag, idx
			)
			self.benchmarking(block=Block(valid=True, tag=tag), idx=idx)

		self.__logger.info('Mapeamento concluído')

		self.misses = (
			self.miss_capacity + self.miss_conflict + self.miss_compulsory
		)

		return (
			self.hits,
			self.misses,
			self.miss_compulsory,
			self.miss_capacity,
			self.miss_conflict,
		)

	def number_of_blocks(self: 'Mapping') -> int:
		"""
		Retorna o número total de blocos no cache.

		:return: Número de blocos no cache.
		"""
		return len(self.sets) * len(self.sets[0])

	def benchmarking(self: 'Mapping', block: Block, idx: int) -> None:
		"""
		Avalia o desempenho do cache verificando se o bloco está presente e
		atualiza os contadores de hits ou de diferentes tipos de misses.

		:param block: Bloco de cache que está sendo verificado.
		:param idx: Índice do conjunto (set) onde o bloco deve estar.
		"""
		if block in self.sets[idx].get_blocks():
			self.__logger.info('Hit no bloco %s', block)
			self.hits += 1
		elif Block() in self.sets[idx].get_blocks():
			self.__logger.warning('Miss compulsório no bloco %s', block)
			self.miss_compulsory += 1
		elif self.miss_compulsory == self.number_of_blocks():
			self.__logger.warning('Miss de capacidade no bloco %s', block)
			self.miss_capacity += 1
		else:
			self.__logger.warning('Miss de conflito no bloco %s', block)
			self.miss_conflict += 1

		self.sets[idx].add_block(block)
