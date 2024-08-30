"""
Módulo de testes para o módulo file.

Este módulo contém testes unitários para a classe File, verificando a leitura de arquivos binários e a validação de caminhos de arquivos.

Classes:
--------
TestFile
    Classe de testes para a classe File.

Funções:
--------
TestFile.__read_txt(path: str) -> List[int]
    Lê o conteúdo de um arquivo de texto e retorna como uma lista de inteiros.

TestFile.test_read_invalid_path(self: Self) -> None
    Testa a leitura de um caminho de arquivo inválido.

TestFile.test_read_invalid_extension(self: Self) -> None
    Testa a leitura de um arquivo com extensão inválida.

TestFile.test_read_valid_file(self: Self) -> None
    Testa a leitura de um arquivo binário válido.

TestFile.test_read_bin_100(self: Self) -> None
    Testa a leitura do arquivo binário 'bin_100.bin' e compara com 'bin_100.txt'.

TestFile.test_read_bin_1000(self: Self) -> None
    Testa a leitura do arquivo binário 'bin_1000.bin' e compara com 'bin_1000.txt'.

TestFile.test_read_bin_10000(self: Self) -> None
    Testa a leitura do arquivo binário 'bin_10000.bin' e compara com 'bin_10000.txt'.

TestFile.test_read_vortex(self: Self) -> None
    Testa a leitura do arquivo binário 'vortex.in.sem.persons.bin' e compara com 'vortex.in.sem.persons.txt'.
"""

from unittest import TestCase, main
from file import File
from typing import Self, List

class TestFile(TestCase):

    @staticmethod
    def read_txt(path: str) -> List[int]:
        """
        Lê o conteúdo de um arquivo de texto e retorna como uma lista de inteiros.

        Parâmetros:
        -----------
        path: str
            Caminho para o arquivo de texto.

        Retorna:
        --------
        List[int]
            Lista de inteiros representando o conteúdo do arquivo.
        """
        arr: List[int] = []

        with open(path, 'r') as f:
            for line in f:
                arr.append(int(line))

        return arr

    def test_read_invalid_path(self: Self) -> None:
        """
        Testa a leitura de um caminho de arquivo inválido.
        """
        file = File.read('')

        self.assertIsNone(file)

    def test_read_invalid_extension(self: Self) -> None:
        """
        Testa a leitura de um arquivo com extensão inválida.
        """
        file = File.read('address/bin_100.txt')

        self.assertIsNone(file)

    def test_read_valid_file(self: Self) -> None:
        """
        Testa a leitura de um arquivo binário válido.
        """
        file = File.read('address/bin_100.bin')

        self.assertIsNotNone(file)

    def test_read_bin_100(self: Self) -> None:
        """
        Testa a leitura do arquivo binário 'bin_100.bin' e compara com 'bin_100.txt'.
        """
        file_bin = File.read('address/bin_100.bin')
        file_txt = self.read_txt('address/bin_100.txt')

        self.assertEqual(file_bin, file_txt)

    def test_read_bin_1000(self: Self) -> None:
        """
        Testa a leitura do arquivo binário 'bin_1000.bin' e compara com 'bin_1000.txt'.
        """
        file_bin = File.read('address/bin_1000.bin')
        file_txt = self.read_txt('address/bin_1000.txt')

        self.assertEqual(file_bin, file_txt)

    def test_read_bin_10000(self: Self) -> None:
        """
        Testa a leitura do arquivo binário 'bin_10000.bin' e compara com 'bin_10000.txt'.
        """
        file_bin = File.read('address/bin_10000.bin')
        file_txt = self.read_txt('address/bin_10000.txt')

        self.assertEqual(file_bin, file_txt)

    def test_read_vortex(self: Self) -> None:
        """
        Testa a leitura do arquivo binário 'vortex.in.sem.persons.bin' e compara com 'vortex.in.sem.persons.txt'.
        """
        file_bin = File.read('address/vortex.in.sem.persons.bin')
        file_txt = self.read_txt('address/vortex.in.sem.persons.txt')

        self.assertEqual(file_bin, file_txt)

if __name__ == '__main__':
    main()
