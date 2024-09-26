from logging import debug, info, warning

from app.cache import Block

from .replacement_policy import ReplacementPolicy


class FIFO(ReplacementPolicy):
	"""Implementa a política de substituição FIFO (First-In, First-Out).

	O elemento mais antigo na lista é removido quando a lista atinge seu limite.
	"""

	@staticmethod
	def add(blocks: list[Block], block: Block) -> list[Block]:
		"""Adiciona um bloco ao conjunto seguindo a política de substituição FIFO.

		Params:
			blocks (list[Block]): Conjunto de blocos existente.
			block (Block): Bloco a ser adicionado.
		Returns:
			list[Block]: Conjunto de blocos atualizado.
		"""  # noqa: E501
		debug(
			'Aplicando política de substituição FIFO em conjunto com '
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
			return blocks

		old_block = tmp[-1]
		tmp = [block] + tmp[: len(tmp) - 1]

		info('Removido bloco %s para inserir o bloco %s', old_block, block)
		return tmp
