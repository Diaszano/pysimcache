from app.replacement_policy import ReplacementPolicyType

from .output_type import OutputType


class Output:
	"""
	Classe responsável por exibir os parâmetros e resultados da simulação
	de mapeamento de cache em diferentes formatos de saída.
	"""

	@staticmethod
	def parameters(
		nsets: int,
		bsize: int,
		assoc: int,
		policy: ReplacementPolicyType,
		file: str,
		output: OutputType,
	) -> None:
		"""
		Exibe os parâmetros da simulação dependendo do tipo de saída especificado.

		:param nsets: Número de conjuntos no cache.
		:param bsize: Tamanho do bloco de cache em bytes.
		:param assoc: Grau de associatividade do cache.
		:param policy: Política de substituição utilizada no cache.
		:param file: Caminho para o arquivo binário de endereços.
		:param output: Tipo de saída (STANDARD ou DETAILED).
		"""  # noqa: E501
		if output == OutputType.STANDARD:
			return

		msg = (
			'Números de conjuntos: %s\n'
			'Tamanho do Bloco: %s\n'
			'Nível de associatividade: %s\n'
			'Política de substituição da cache: %s\n'
			'Caminho para o arquivo: %s\n'
		)

		msg = msg % (nsets, bsize, assoc, policy.name, file)
		print(msg)

	@staticmethod
	def results(
		hits: int,
		misses: int,
		miss_compulsory: int,
		miss_capacity: int,
		miss_conflict: int,
		output: OutputType,
	) -> None:
		"""
		Exibe os resultados da simulação de cache, incluindo as taxas de acertos
		e diferentes tipos de erros (misses), conforme o tipo de saída.

		:param hits: Número de acertos (hits) durante o mapeamento.
		:param misses: Número total de erros (misses).
		:param miss_compulsory: Número de erros compulsórios (compulsory misses).
		:param miss_capacity: Número de erros de capacidade (capacity misses).
		:param miss_conflict: Número de erros de conflito (conflict misses).
		:param output: Tipo de saída (STANDARD ou DETAILED).
		"""  # noqa: E501
		access = hits + misses
		hits_rate = hits / access
		misses_rate = misses / access
		miss_compulsory_rate = miss_compulsory / misses
		miss_capacity_rate = miss_capacity / misses
		miss_conflict_rate = miss_conflict / misses

		if output == OutputType.STANDARD:
			msg = '%s %.4f %.4f %.2f %.2f %.2f' % (
				access,
				hits_rate,
				misses_rate,
				miss_compulsory_rate,
				miss_capacity_rate,
				miss_conflict_rate,
			)
		else:
			msg = (
				'RESULTADOS:\n'
				'Números de acessos: \t%s\n'
				'Taxa de acertos (hit): \t%.4f | %.2f%%\n'
				'Taxa de erros (miss): \t%.4f | %.2f%%\n\t'
				'Compulsórios: \t%.2f | %.2f%%\n\t'
				'Capacidade: \t%.2f | %.2f%%\n\t'
				'Conflito: \t%.2f | %.2f%%'
			) % (
				access,
				hits_rate,
				hits_rate * 100,
				misses_rate,
				misses_rate * 100,
				miss_compulsory_rate,
				miss_compulsory_rate * 100,
				miss_capacity_rate,
				miss_capacity_rate * 100,
				miss_conflict_rate,
				miss_conflict_rate * 100,
			)
		print(msg)
