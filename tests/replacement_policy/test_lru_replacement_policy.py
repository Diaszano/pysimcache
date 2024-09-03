from random import randint, sample
from unittest import TestCase

from app.replacement_policy.lru_replacement_policy import LRUReplacementPolicy


class TestLRUReplacementPolicy(TestCase):
	"""Testa a classe LRUReplacementPolicy, que implementa a política de substituição LRU (Least Recently Used)."""  # noqa: E501

	def test_add_new_element_to_non_empty_list(
		self: 'TestLRUReplacementPolicy',
	) -> None:
		"""
		Testa se ao adicionar um novo elemento a uma lista não vazia, a lista mantém o tamanho correto.

		Verifica se o novo elemento é adicionado e o tamanho da lista continua o mesmo,
		removendo o elemento menos recentemente usado se necessário.
		"""  # noqa: E501
		block = sample(range(10), k=5)
		new_number = randint(10, 20)

		result = LRUReplacementPolicy.add(block=block, new=new_number)

		self.assertIn(new_number, result)
		self.assertEqual(len(result), len(block))

	def test_add_existing_element_to_list(
		self: 'TestLRUReplacementPolicy',
	) -> None:
		"""
		Testa se ao adicionar um elemento já existente na lista, o tamanho da lista permanece o mesmo.

		Verifica se o elemento é movido para o início da lista, mantendo o tamanho original.
		"""  # noqa: E501
		block = sample(range(10), k=5)
		existing_number = block[randint(0, 4)]

		result = LRUReplacementPolicy.add(block=block, new=existing_number)

		self.assertIn(existing_number, result)
		self.assertEqual(len(result), len(block))
		self.assertEqual(result[0], existing_number)

	def test_add_element_to_empty_list(
		self: 'TestLRUReplacementPolicy',
	) -> None:
		"""
		Testa se ao adicionar um novo elemento em uma lista vazia, o tamanho da lista se torna 1.

		Verifica se o novo elemento é corretamente adicionado à lista que estava vazia.
		"""  # noqa: E501
		block = []
		new_number = randint(10, 20)

		result = LRUReplacementPolicy.add(block=block, new=new_number)

		self.assertEqual(len(result), 1)
		self.assertIn(new_number, result)

	def test_repeated_element_moves_to_front(
		self: 'TestLRUReplacementPolicy',
	) -> None:
		"""
		Testa se um elemento repetido é movido para o início da lista.

		Verifica se a política LRU move o elemento recém-utilizado para o topo da lista.
		"""  # noqa: E501
		block = sample(range(10), k=randint(2, 5))
		repeated_number = block[randint(0, len(block) - 1)]

		result = LRUReplacementPolicy.add(block=block, new=repeated_number)

		self.assertIn(repeated_number, result)
		self.assertEqual(result[0], repeated_number)
		self.assertEqual(len(result), len(block))

	def test_oldest_element_removed_when_list_is_full(
		self: 'TestLRUReplacementPolicy',
	) -> None:
		"""
		Testa se o elemento mais antigo é removido quando a lista atinge seu tamanho máximo.

		Verifica se, ao adicionar um novo elemento a uma lista cheia, o elemento menos recentemente usado é removido.
		"""  # noqa: E501
		block = sample(range(10), k=randint(2, 5))
		new_number = randint(10, 20)

		result = LRUReplacementPolicy.add(block=block, new=new_number)

		self.assertNotIn(block[-1], result)
		self.assertIn(new_number, result)
		self.assertEqual(len(result), len(block))
