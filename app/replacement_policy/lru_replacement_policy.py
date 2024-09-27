from logging import debug, info, warning

from app.cache import Block

from .replacement_policy import ReplacementPolicy


class LRU(ReplacementPolicy):
	"""Implementa a política de substituição LRU (Least Recently Used).

	O bloco menos recentemente utilizado no conjunto é removido quando o conjunto atinge seu limite.
	"""  # noqa: E501

	@staticmethod
	def add(blocks: list[Block], block: Block) -> list[Block]:
		"""Adiciona um bloco ao conjunto seguindo a política de substituição LRU.

		Params:
			blocks (list[Block]): Conjunto de blocos existente.
			block (Block): Bloco a ser adicionado.
		Returns:
			list[Block]: Conjunto de blocos atualizado.
		"""  # noqa: E501
		debug(
			'Aplicando política de substituição LRU em conjunto com '
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
			tmp.remove(block)
			tmp.append(block)
			return tmp

		old_block = tmp.pop(0)
		tmp.append(block)

		info('Removido bloco %s para inserir o bloco %s', old_block, block)
		return tmp
