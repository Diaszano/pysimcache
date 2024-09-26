from logging import debug, info, warning
from random import randint

from app.cache import Block

from .replacement_policy import ReplacementPolicy


class Random(ReplacementPolicy):
	"""Implementa a política de substituição Random.

	Um bloco aleatório do conjunto é removido quando o conjunto atinge seu limite.
	"""  # noqa: E501

	@staticmethod
	def add(blocks: list[Block], block: Block) -> list[Block]:
		"""Adiciona um bloco ao conjunto seguindo a política de substituição Random.

		Params:
			blocks (list[Block]): Conjunto de blocos existente.
			block (Block): Bloco a ser adicionado.
		Returns:
			list[Block]: Conjunto de blocos atualizado.
		"""  # noqa: E501
		debug(
			'Aplicando política de substituição Random em conjunto com '
			'%s blocos para adicionar o bloco %s',
			len(blocks),
			block,
		)
		tmp = blocks.copy()

		if len(tmp) == 0:
			warning(msg='Conjunto de blocos está vazio')
			return []

		if block in tmp:
			info('Bloco %s já existe no conjunto', block)
			return tmp

		position = Random.__get_index(blocks=blocks)

		old_block = tmp[position]
		tmp[position] = block

		info('Removido bloco %s para inserir o bloco %s', old_block, block)
		return tmp

	@staticmethod
	def __get_index(blocks: list[Block]) -> int:
		"""
		Retorna o índice do primeiro bloco inválido no conjunto ou um índice aleatório.

		Params:
			blocks: Conjunto de blocos.
		Params:
			int: Índice do primeiro bloco inválido (ou None se não houver) ou um índice aleatório.
		"""  # noqa: E501

		for i in range(len(blocks)):
			if not blocks[i].valid:
				debug('Bloco inválido encontrado na posição %s', i)
				return i

		random_index = randint(a=0, b=len(blocks) - 1)
		debug('Índice aleatório gerado: %s', random_index)

		return random_index
