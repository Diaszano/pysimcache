from .replacement_policy import ReplacementPolicy


class LRUReplacementPolicy(ReplacementPolicy):
	"""Implementa a política de substituição LRU (Least Recently Used).
	O elemento menos recentemente utilizado é removido quando a lista atinge seu limite.
	"""  # noqa: E501

	@staticmethod
	def add(block: list[any], new: any) -> list[any]:
		"""Adiciona um novo elemento à lista usando a política LRU.

		Se a lista estiver vazia, o novo elemento será o único na lista.
		Se o elemento já estiver na lista, ele será removido de sua posição original e movido para o início da lista, representando o uso recente.
		Se a lista estiver cheia e o elemento for novo, o elemento menos recentemente utilizado (último da lista) será removido e o novo será adicionado ao início.

		Args:
		----
			block (list[any]): A lista de elementos atuais.
			new (any): O novo elemento a ser adicionado.

		Returns:
		-------
			list[any]: A nova lista após aplicar a política de substituição LRU.

		"""  # noqa: E501
		tmp = block.copy()

		if len(tmp) == 0:
			return [new]

		if new in tmp:
			tmp.remove(new)
			return [new] + tmp[:]

		return [new] + tmp[: len(tmp) - 1]
