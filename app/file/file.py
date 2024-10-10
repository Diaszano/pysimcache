from logging import getLogger
from pathlib import Path
from typing import Generator


class File:
	"""Classe utilitária para manipulação de arquivos binários."""

	_logger = getLogger(name=__name__)

	@staticmethod
	def read_bin_file(
		path: str, address_size: int = 32
	) -> Generator[int, None, None] | None:
		"""
		Lê um arquivo binário e retorna uma lista de endereços como inteiros.

		Args:
			path (str): O caminho para o arquivo binário a ser lido.
			address_size (int, opcional): O tamanho do endereço em bits. O valor padrão é 32 bits.

		Returns:
			Generator[int] | None: Um Generator de endereços inteiros se o arquivo for válido, ou None se o arquivo não for válido.
		"""  # noqa: E501
		if not File.is_valid_bin_file(path=path):
			File._logger.critical(
				'Não foi possível ler o arquivo binário "%s". Motivo: o arquivo é inválido ou não atende aos requisitos esperados.',  # noqa: E501
				path,
			)
			return None

		with Path(path).open(mode='rb') as file:
			while address := file.read(int(address_size / 8)):
				yield int.from_bytes(address, byteorder='big')

		File._logger.info(
			'Leitura do arquivo "%s" concluída com sucesso.', path
		)

	@staticmethod
	def is_valid_file(path: str) -> bool:
		"""
		Verifica se o arquivo existe e não está vazio.

		Args:
			path (str): O caminho do arquivo a ser verificado.

		Returns:
			bool: True se o arquivo existir e não estiver vazio, False caso contrário.
		"""  # noqa: E501
		is_valid = Path(path).exists() and not File.is_file_empty(path=path)

		if is_valid:
			File._logger.info('O arquivo "%s" foi validado com sucesso.', path)
		else:
			File._logger.warning(
				'Falha na validação do arquivo "%s". Verifique se o caminho está correto e se o arquivo não está vazio.',  # noqa: E501
				path,
			)

		return is_valid

	@staticmethod
	def is_valid_bin_file(path: str) -> bool:
		"""
		Verifica se o arquivo é um arquivo binário válido.

		Um arquivo binário válido é aquele que existe, não está vazio e tem a extensão '.bin'.

		Args:
			path (str): O caminho do arquivo binário a ser verificado.

		Returns:
			bool: True se o arquivo for um binário válido, False caso contrário.
		"""  # noqa: E501
		is_valid = File.is_valid_file(path=path) and Path(path).suffix == '.bin'

		if is_valid:
			File._logger.info(
				'O arquivo binário "%s" é válido e está pronto para leitura.',
				path,
			)
		else:
			File._logger.warning(
				'O arquivo binário "%s" é inválido. Certifique-se de que ele existe, não está vazio e possui a extensão ".bin".',  # noqa: E501
				path,
			)

		return is_valid

	@staticmethod
	def is_file_empty(path: str) -> bool:
		"""
		Verifica se o arquivo está vazio.

		Args:
			path (str): O caminho do arquivo a ser verificado.

		Returns:
			bool: True se o arquivo estiver vazio, False caso contrário.
		"""
		file_size = Path(path).stat().st_size
		is_empty = file_size == 0

		if is_empty:
			File._logger.warning(
				'O arquivo "%s" está vazio! Tamanho: %d bytes.', path, file_size
			)
		else:
			File._logger.info(
				'O arquivo "%s" não está vazio. Tamanho: %d bytes.',
				path,
				file_size,
			)
		return is_empty
