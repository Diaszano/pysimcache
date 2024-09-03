from random import randint
from unittest import TestCase

from app.replacement_policy import FIFOReplacementPolicy


class TestFifoReplacementPolicy(TestCase):
	def test_fifo_replacement_policy_with_nonexistent_element(
		self: 'TestFifoReplacementPolicy',
	) -> None:
		"""
		Testa a política de substituição FIFO ao adicionar um novo elemento
		a uma lista que não contém o novo elemento.

		Verifica se o novo elemento é adicionado e o elemento mais antigo é removido
		quando a lista está cheia.
		"""  # noqa: E501
		block = [0, 1, 2, 3]
		number = randint(4, 9)

		result = FIFOReplacementPolicy.add(block, number)

		self.assertIn(number, result)
		self.assertEqual(len(result), len(block))

	def test_fifo_replacement_policy_with_existing_element(
		self: 'TestFifoReplacementPolicy',
	) -> None:
		"""
		Testa a política de substituição FIFO ao tentar adicionar um elemento
		que já está presente na lista.

		Verifica se a lista não é alterada quando o elemento já existe.
		"""
		block = [0, 1, 2, 3]
		number = randint(0, 3)

		result = FIFOReplacementPolicy.add(block, number)

		self.assertIn(number, result)
		self.assertEqual(len(result), len(block))
		self.assertEqual(block, result)

	def test_fifo_replacement_policy_with_empty_list(
		self: 'TestFifoReplacementPolicy',
	) -> None:
		"""
		Testa a política de substituição FIFO ao adicionar um elemento
		a uma lista vazia.

		Verifica se o novo elemento é o único na lista resultante.
		"""
		block = []
		number = randint(0, 9)

		result = FIFOReplacementPolicy.add(block, number)

		self.assertIn(number, result)
		self.assertEqual(len(result), 1)

	def test_fifo_replacement_policy_with_single_element_list(
		self: 'TestFifoReplacementPolicy',
	) -> None:
		"""
		Testa a política de substituição FIFO ao adicionar um novo elemento
		a uma lista que já contém um único elemento.

		Verifica se o novo elemento é adicionado e o elemento original é removido
		quando a lista está cheia.
		"""  # noqa: E501
		block = [0]
		number = 1

		result = FIFOReplacementPolicy.add(block, number)

		self.assertIn(number, result)
		self.assertEqual(len(result), 1)
		self.assertNotIn(block[0], result)
