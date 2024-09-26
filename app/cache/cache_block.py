class Block:
	"""Representa uma unidade de memória da cache."""

	def __init__(self: 'Block', valid: bool = False, tag: int = 0) -> None:
		"""
		Inicializa a instância do bloco.

		Args:
			valid (bool): Sinalizando se o bloco está válido ou não.
			tag (int): Código de endereço associado ao bloco.

		Returns:
			None
		"""
		self.valid = valid
		self.tag = tag

	def __eq__(self: 'Block', other: 'Block') -> bool:
		"""
		Compara dois blocos se são iguais.

		Args:
			other: Outra instância do bloco para comparar com o presente.

		Returns:
			bool: Verdadeiro se os dois blocos forem iguais.
		"""
		return self.tag == other.tag and self.valid == other.valid

	def __gt__(self: 'Block', other: 'Block') -> bool:
		"""
		Compara dois blocos se o presente é maior que outro.

		Args:
			other: Outra instância do bloco para comparar com o presente.

		Returns:
			bool: Verdadeiro se o presente for maior que outro.
		"""
		return self.tag > other.tag

	def __lt__(self: 'Block', other: 'Block') -> bool:
		"""
		Compara dois blocos se o presente é menor que outro.

		Args:
			other: Outra instância do bloco para comparar com o presente.

		Returns:
			bool: Verdadeiro se o presente for menor que outro.
		"""
		return self.tag < other.tag

	def __ge__(self: 'Block', other: 'Block') -> bool:
		"""
		Compara dois blocos se o presente é maior ou igual a outro.

		Args:
			other: Outra instância do bloco para comparar com o presente.

		Returns:
			bool: Verdadeiro se o presente for maior ou igual a outro.
		"""
		return self.tag >= other.tag

	def __le__(self: 'Block', other: 'Block') -> bool:
		"""
		Compara dois blocos se o presente é menor ou igual a outro.

		Args:
			other: Outra instância do bloco para comparar com o presente.

		Returns:
			bool: Verdadeiro se o presente for menor ou igual a outro.
		"""
		return self.tag <= other.tag

	def __ne__(self: 'Block', other: 'Block') -> bool:
		"""
		Compara dois blocos se são diferentes.

		Args:
			other: Outra instância do bloco para comparar com o presente.

		Returns:
			bool: Verdadeiro se os dois blocos forem diferentes.
		"""
		return not self == other

	def __str__(self: 'Block') -> str:
		"""
		Retorna uma representação string da instância do bloco.

		Returns:
			str: Representação string da instância.
		"""
		return f'{{Tag: {self.tag}, Valid: {self.valid}}}'

	def __repr__(self: 'Block') -> str:
		"""
		Retorna uma representação string da instância do bloco para fins de depuração.

		Returns:
			str: Representação string da instância para fins de depuração.
		"""  # noqa: E501
		return f'{{Tag: {self.tag}, Valid: {self.valid}}}'
