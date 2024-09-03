from random import randint
from unittest import TestCase

from app.replacement_policy import RandomReplacementPolicy


class TestRandomReplacementPolicy(TestCase):
	"""Testa a classe RandomReplacementPolicy, que implementa a política de substituição aleatória."""  # noqa: E501

	def test_add_to_empty_list(self: 'TestRandomReplacementPolicy') -> None:
		"""
		Testa a política de substituição aleatória ao adicionar um novo elemento a uma lista vazia.

		Verifica se o novo elemento é o único na lista resultante.
		"""  # noqa: E501
		block = []
		number = randint(25, 50)
		result = RandomReplacementPolicy.add(block, number)

		self.assertEqual(len(result), 1)
		self.assertIn(number, result)

	def test_add_to_single_element_list(
		self: 'TestRandomReplacementPolicy',
	) -> None:
		"""
		Testa a política de substituição aleatória ao adicionar um novo elemento a uma lista com um único elemento.

		Verifica se o novo elemento substitui o único elemento existente.
		"""  # noqa: E501
		block = [1]
		number = randint(25, 50)
		result = RandomReplacementPolicy.add(block, number)

		self.assertEqual(len(result), 1)
		self.assertIn(number, result)
		self.assertNotIn(1, result)

	def test_add_existing_element(self: 'TestRandomReplacementPolicy') -> None:
		"""
		Testa a política de substituição aleatória ao tentar adicionar um elemento que já está na lista.

		Verifica se a lista permanece inalterada.
		"""  # noqa: E501
		block = [0, 1, 2, 3, 4]
		existing_number = block[randint(0, len(block) - 1)]
		result = RandomReplacementPolicy.add(block, existing_number)

		self.assertEqual(result, block)

	def test_add_new_element_to_full_list(
		self: 'TestRandomReplacementPolicy',
	) -> None:
		"""
		Testa a política de substituição aleatória ao adicionar um novo elemento a uma lista cheia.

		Verifica se o novo elemento substitui um elemento existente aleatoriamente e que o novo elemento está na lista.
		"""  # noqa: E501
		block = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
		number = randint(25, 50)
		result = RandomReplacementPolicy.add(block, number)

		self.assertIn(number, result)
		self.assertEqual(len(result), len(block))
		self.assertNotIn(block[result.index(number)], result)

	def test_random_replacement_policy_does_not_change_list_size(
		self: 'TestRandomReplacementPolicy',
	) -> None:
		"""
		Testa a política de substituição aleatória para garantir que o tamanho da lista permaneça o mesmo
		após a adição de um novo elemento, quando a lista não está vazia e o novo elemento é diferente.
		"""  # noqa: E501
		block = [0, 1, 2, 3, 4, 5]
		new_element = randint(20, 30)

		result = RandomReplacementPolicy.add(block, new_element)

		self.assertIn(new_element, result)
		self.assertEqual(len(result), len(block))
		self.assertNotEqual(result, block)
