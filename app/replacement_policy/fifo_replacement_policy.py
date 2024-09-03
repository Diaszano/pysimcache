from .replacement_policy import ReplacementPolicy


class FIFOReplacementPolicy(ReplacementPolicy):
	"""Implementa a política de substituição FIFO (First-In, First-Out).
	O elemento mais antigo na lista é removido quando a lista atinge seu limite.
	"""

	@staticmethod
	def add(block: list[any], new: any) -> list[any]:
		"""Adiciona um novo elemento à lista usando a política FIFO.

		Se a lista estiver vazia, o novo elemento será o único da lista.
		Se o elemento já estiver na lista, a lista não será alterada.
		Se a lista estiver cheia, o elemento mais antigo será removido e o novo será adicionado ao início da lista.

		Args:
		----
			block (list[any]): A lista de elementos atuais.
			new (any): O novo elemento a ser adicionado.

		Returns:
		-------
			list[any]: A nova lista após aplicar a política de substituição.

		"""  # noqa: E501
		tmp = block.copy()

		if len(tmp) == 0:
			return [new]

		if new in tmp:
			return tmp

		return [new] + tmp[: len(tmp) - 1]
