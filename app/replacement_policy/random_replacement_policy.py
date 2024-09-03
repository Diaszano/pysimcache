from random import randint

from .replacement_policy import ReplacementPolicy


class RandomReplacementPolicy(ReplacementPolicy):
	"""Implementa a política de substituição aleatória (Random Replacement Policy).
	Um elemento existente é substituído por um novo em uma posição aleatória.
	"""  # noqa: E501

	@staticmethod
	def add(block: list[any], new: any) -> list[any]:
		"""Adiciona um novo elemento à lista usando a política de substituição aleatória.

		Se a lista estiver vazia ou tiver apenas um elemento, o novo elemento será o único na lista.
		Se o novo elemento já estiver na lista, não haverá mudanças.
		Se o novo elemento for diferente, ele substituirá um elemento existente em uma posição aleatória da lista.

		Args:
		----
			block (list[any]): A lista de elementos atuais.
			new (any): O novo elemento a ser adicionado.

		Returns:
		-------
			list[any]: A nova lista após aplicar a política de substituição aleatória.

		"""  # noqa: E501
		tmp = block.copy()

		if len(tmp) == 0 or len(tmp) == 1:
			return [new]

		if new in tmp:
			return tmp

		tmp[randint(a=0, b=len(tmp) - 1)] = new

		return tmp
