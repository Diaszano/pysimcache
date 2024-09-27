from logging import getLogger

from app.cache import Block

from .replacement_policy import ReplacementPolicy


class FIFO(ReplacementPolicy):
	"""Implementa a política de substituição FIFO (First-In, First-Out).

	O bloco mais antigo no conjunto é removido quando o conjunto atinge seu limite.
	"""  # noqa: E501

	__logger = getLogger(name=__name__)

	@staticmethod
	def add(blocks: list[Block], block: Block) -> list[Block]:
		"""Adiciona um bloco ao conjunto seguindo a política de substituição FIFO.

		Params:
			blocks (list[Block]): Conjunto de blocos existente.
			block (Block): Bloco a ser adicionado.
		Returns:
			list[Block]: Conjunto de blocos atualizado.
		"""  # noqa: E501
		FIFO.__logger.debug(
			'Aplicando política de substituição FIFO em conjunto com '
			'%s blocos para adicionar o bloco %s',
			len(blocks),
			block,
		)

		tmp = blocks.copy()

		if not block.valid:
			FIFO.__logger.warning('O bloco %s é inválido', block)
			return tmp

		if len(tmp) == 0:
			FIFO.__logger.warning(msg='Conjunto de blocos está vazio')
			return tmp

		if block in tmp:
			FIFO.__logger.info('Bloco %s já existe no conjunto', block)
			return tmp

		old_block = tmp.pop(0)
		tmp.append(block)

		FIFO.__logger.info(
			'Removido bloco %s para inserir o bloco %s', old_block, block
		)
		return tmp
