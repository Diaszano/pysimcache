from pathlib import Path


class File:
	"""
	Classe utilitária para manipulação de arquivos binários.

	Contém métodos para ler arquivos binários e verificar a validade e integridade de arquivos.
	"""  # noqa: E501

	@staticmethod
	def read_bin_file(
		path: str,
		address_size: int = 32,
	) -> list[int] | None:
		"""
		Lê um arquivo binário e retorna uma lista de endereços como inteiros.

		Este método lê o arquivo binário no caminho fornecido e divide seu conteúdo
		em blocos de tamanho `address_size`. Cada bloco é convertido em um inteiro
		e adicionado a uma lista.

		Args:
			path (str): O caminho para o arquivo binário a ser lido.
			address_size (int, opcional): O tamanho do endereço em bits. O valor padrão é 32 bits.

		Returns:
			list[int] | None: Uma lista de endereços inteiros se o arquivo for válido, ou None se o arquivo não for válido.
		"""  # noqa: E501
		if not File.is_valid_bin_file(path=path):
			return None

		address_array: list[int] = []
		with Path(path).open(mode='rb') as file:
			while address := file.read(int(address_size / 8)):
				address_array.append(int.from_bytes(address))

		return address_array

	@staticmethod
	def is_valid_file(path: str) -> bool:
		"""
		Verifica se o arquivo existe e não está vazio.

		Args:
			path (str): O caminho do arquivo a ser verificado.

		Returns:
			bool: True se o arquivo existir e não estiver vazio, False caso contrário.
		"""  # noqa: E501
		return Path(path).exists() and not File.is_file_empty(path=path)

	@staticmethod
	def is_valid_bin_file(path: str) -> bool:
		"""
		Verifica se o arquivo é um arquivo binário válido.

		Um arquivo binário válido é aquele que existe, não está vazio, e tem a extensão '.bin'.

		Args:
			path (str): O caminho do arquivo binário a ser verificado.

		Returns:
			bool: True se o arquivo for um binário válido, False caso contrário.
		"""  # noqa: E501
		return File.is_valid_file(path=path) and path.endswith('.bin')

	@staticmethod
	def is_file_empty(path: str) -> bool:
		"""
		Verifica se o arquivo está vazio.

		Args:
			path (str): O caminho do arquivo a ser verificado.

		Returns:
			bool: True se o arquivo estiver vazio, False caso contrário.
		"""
		return Path(path).stat().st_size == 0
