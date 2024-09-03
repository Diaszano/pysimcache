from pathlib import Path
from unittest import TestCase

from app.file import File


class TestFile(TestCase):
	@staticmethod
	def read_txt(path: str) -> list[int]:
		"""
		Lê o conteúdo de um arquivo de texto e retorna como uma lista de inteiros.

		Parâmetros:
		-----------
		path: str
			Caminho para o arquivo de texto.

		Retorna:
		--------
		list[int]
			Lista de inteiros representando o conteúdo do arquivo.
		"""  # noqa: E501
		with Path(path).open(mode='r') as f:
			return [int(line) for line in f]

	def test_read_bin_file_with_invalid_path(self: 'TestFile') -> None:
		"""
		Testa a função `read_bin_file` com um caminho de arquivo inválido.

		Verifica se a função retorna `None` quando fornecido um caminho vazio,
		o que indica que o arquivo não pôde ser encontrado ou lido.
		"""
		file = File.read_bin_file('')
		self.assertIsNone(file)

	def test_read_bin_file_with_invalid_extension(self: 'TestFile') -> None:
		"""
		Testa a função `read_bin_file` com uma extensão de arquivo inválida.

		Verifica se a função retorna `None` quando o arquivo possui uma extensão
		diferente de '.bin'.
		"""
		file = File.read_bin_file('address/bin_100.txt')
		self.assertIsNone(file)

	def test_read_bin_file_with_valid_file(self: 'TestFile') -> None:
		"""
		Testa a função `read_bin_file` com um arquivo binário válido.

		Verifica se a função retorna uma lista de inteiros ao ler um arquivo binário
		válido.
		"""  # noqa: E501
		file = File.read_bin_file('address/bin_100.bin')
		self.assertIsNotNone(file)

	def test_read_bin_file_comparison_bin_100(self: 'TestFile') -> None:
		"""
		Testa a leitura do arquivo binário 'bin_100.bin' e compara com 'bin_100.txt'.

		Verifica se o conteúdo lido do arquivo binário corresponde ao conteúdo
		do arquivo de texto esperado.
		"""  # noqa: E501
		file_bin = File.read_bin_file('address/bin_100.bin')
		file_txt = self.read_txt('address/bin_100.txt')
		self.assertEqual(file_bin, file_txt)

	def test_read_bin_file_comparison_bin_1000(self: 'TestFile') -> None:
		"""
		Testa a leitura do arquivo binário 'bin_1000.bin' e compara com 'bin_1000.txt'.

		Verifica se o conteúdo lido do arquivo binário corresponde ao conteúdo
		do arquivo de texto esperado.
		"""  # noqa: E501
		file_bin = File.read_bin_file('address/bin_1000.bin')
		file_txt = self.read_txt('address/bin_1000.txt')
		self.assertEqual(file_bin, file_txt)

	def test_read_bin_file_comparison_bin_10000(self: 'TestFile') -> None:
		"""
		Testa a leitura do arquivo binário 'bin_10000.bin' e compara com 'bin_10000.txt'.

		Verifica se o conteúdo lido do arquivo binário corresponde ao conteúdo
		do arquivo de texto esperado.
		"""  # noqa: E501
		file_bin = File.read_bin_file('address/bin_10000.bin')
		file_txt = self.read_txt('address/bin_10000.txt')
		self.assertEqual(file_bin, file_txt)

	def test_read_bin_file_comparison_vortex(self: 'TestFile') -> None:
		"""
		Testa a leitura do arquivo binário 'vortex.in.sem.persons.bin' e compara com 'vortex.in.sem.persons.txt'.

		Verifica se o conteúdo lido do arquivo binário corresponde ao conteúdo
		do arquivo de texto esperado.
		"""  # noqa: E501
		file_bin = File.read_bin_file('address/vortex.in.sem.persons.bin')
		file_txt = self.read_txt('address/vortex.in.sem.persons.txt')
		self.assertEqual(file_bin, file_txt)

	def test_read_empty_bin_file(self: 'TestFile') -> None:
		"""
		Testa a função `read_bin_file` ao tentar ler um arquivo binário vazio.

		Verifica se a função retorna `None` ao ler um arquivo binário que está vazio.
		"""  # noqa: E501
		file = File.read_bin_file('address/empty.bin')
		self.assertIsNone(file)

	def test_read_nonexistent_file(self: 'TestFile') -> None:
		"""
		Testa a função `read_bin_file` com um arquivo que não existe.

		Verifica se a função retorna `None` quando o arquivo binário não é encontrado.
		"""  # noqa: E501
		file = File.read_bin_file('address/nonexistent.bin')
		self.assertIsNone(file)
