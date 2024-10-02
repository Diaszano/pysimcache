from random import randint, sample
from unittest import TestCase

from app.cache import Block
from app.replacement_policy import Random


class TestRandomReplacementPolicy(TestCase):
	def test_empty_set_with_nonexistent_block(
		self: 'TestRandomReplacementPolicy',
	) -> None:
		"""
		Testa a adição de um bloco em um conjunto vazio.

		Verifica:
		- Se o bloco não é adicionado, pois o tamanho máximo é zero.
		- Se o comprimento da lista permanece o mesmo.
		"""
		block = Block(valid=True, tag=randint(a=1, b=5))
		blocks: list[Block] = []

		result = Random.add(blocks=blocks, block=block)

		self.assertNotIn(member=block, container=result)
		self.assertEqual(first=len(blocks), second=len(result))

	def test_single_block_addition(self: 'TestRandomReplacementPolicy') -> None:
		"""
		Testa a adição de um bloco em um conjunto com um único bloco.

		Verifica:
		- Se o novo bloco é adicionado ao conjunto.
		- Se o comprimento do conjunto permanece igual.
		"""
		block = Block(valid=True, tag=randint(a=1, b=5))
		blocks = [Block(valid=True, tag=randint(a=6, b=10))]

		result = Random.add(blocks=blocks, block=block)

		self.assertIn(member=block, container=result)
		self.assertEqual(first=len(blocks), second=len(result))

	def test_adding_existing_block(self: 'TestRandomReplacementPolicy') -> None:
		"""
		Testa a adição de um bloco que já está presente no conjunto.

		Verifica:
		- Se o novo bloco permanece no conjunto.
		- Se o comprimento do conjunto permanece igual.
		- Se o conjunto permanece idêntico.
		"""
		block = Block(valid=True, tag=randint(a=1, b=5))
		blocks = [Block(valid=True, tag=randint(a=6, b=10)), block]

		result = Random.add(blocks=blocks, block=block)

		self.assertIn(member=block, container=result)
		self.assertEqual(first=len(result), second=len(blocks))
		self.assertEqual(first=block, second=result[1])
		self.assertEqual(first=blocks, second=result)

	def test_three_blocks_replacement(
		self: 'TestRandomReplacementPolicy',
	) -> None:
		"""
		Testa a substituição FIFO quando há três blocos no conjunto.

		Verifica:
		- Se o novo bloco está presente na lista.
		- Se o comprimento do conjunto permanece igual.
		"""
		block = Block(valid=True, tag=randint(a=10, b=20))

		blocks = [
			Block(valid=True, tag=tag)
			for tag in sample(population=range(10), k=3)
		]

		result = Random.add(blocks=blocks, block=block)

		self.assertIn(member=block, container=result)
		self.assertEqual(first=len(result), second=len(blocks))

	def test_complete_replacement(self: 'TestRandomReplacementPolicy') -> None:
		"""
		Testa a substituição dos blocos no conjunto.

		Adiciona a mesma quantidade de blocos no conjunto.

		Verifica:
		- Se os novos blocos estão presentes no conjunto.
		- Se nenhum bloco inicial permanece no conjunto.
		"""
		capacity = randint(a=3, b=9)

		blocks = [
			Block(valid=True, tag=tag)
			for tag in sample(population=range(10), k=capacity)
		]

		new_blocks = [
			Block(valid=True, tag=tag + 10)
			for tag in sample(population=range(10), k=capacity)
		]

		result = blocks.copy()

		for block in new_blocks:
			result = Random.add(blocks=result, block=block)

		self.assertEqual(first=len(result), second=capacity)

	def test_adding_invalid_block(self: 'TestRandomReplacementPolicy') -> None:
		"""
		Testa a adição de um bloco inválido ao conjunto.

		Verifica:
		- Se o bloco inválido não é adicionado ao conjunto.
		- Se o comprimento do conjunto permanece o mesmo.
		"""
		invalid_block = Block(valid=False, tag=randint(a=1, b=5))
		blocks = [Block(valid=True, tag=randint(a=6, b=10))]

		result = Random.add(blocks=blocks, block=invalid_block)

		self.assertNotIn(member=invalid_block, container=result)
		self.assertEqual(first=len(blocks), second=len(result))

	def test_remove_all_invalid_block(
		self: 'TestRandomReplacementPolicy',
	) -> None:
		"""
		Testa a remoção de todos os blocos inválidos do conjunto.

		Verifica:
		- Se não tem mais blocos inválidos no conjunto.
		- Se o conjunto mantêm o mesmo tamanho.
		"""
		capacity = randint(a=3, b=9)
		invalid_blocks = [
			Block(tag=tag) for tag in sample(population=range(10), k=capacity)
		]

		valid_blocks = [
			Block(valid=True, tag=tag)
			for tag in sample(population=range(10), k=capacity)
		]

		result = invalid_blocks.copy()

		for block in valid_blocks:
			result = Random.add(blocks=result, block=block)

		for block in invalid_blocks:
			self.assertNotIn(member=block, container=result)
