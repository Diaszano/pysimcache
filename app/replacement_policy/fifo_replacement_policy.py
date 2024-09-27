from logging import debug, info, warning

from app.cache import Block

from .replacement_policy import ReplacementPolicy


class FIFO(ReplacementPolicy):
	"""Implementa a política de substituição FIFO (First-In, First-Out).

	O bloco mais antigo no conjunto é removido quando o conjunto atinge seu limite.
	"""  # noqa: E501

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

		if not block.valid:
			warning('O bloco %s é inválido', block)
			return tmp

		if len(tmp) == 0:
			warning(msg='Conjunto de blocos está vazio')
			return tmp

		if block in tmp:
			info('Bloco %s já existe no conjunto', block)
			return tmp

		old_block = tmp.pop(__index=0)
		tmp.append(__object=block)

		info('Removido bloco %s para inserir o bloco %s', old_block, block)
		return tmp
