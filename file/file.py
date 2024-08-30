"""
Módulo para manipulação de arquivos binários.

Este módulo fornece uma classe `File` com métodos para leitura de arquivos binários.

Classes:
--------
File
    Classe para manipulação de arquivos binários.

Funções:
--------
File.read(path: str) -> Union[List[int], None]
    Lê o conteúdo de um arquivo binário e retorna como uma lista de inteiros.
"""
from os.path import exists
from typing import Union, List


class File:
    """
    Classe para manipulação de arquivos binários.

    Atributos:
    ----------
    __address_size : int
        Tamanho do endereço em bits. Padrão é 32 bits.
    """
    __address_size = 32

    @staticmethod
    def read(path: str) -> Union[List[int], None]:
        """
        Lê o conteúdo de um arquivo binário e retorna como uma lista de inteiros.

        Parâmetros:
        -----------
        path: str
            Caminho para o arquivo binário.

        Retorna:
        --------
        Union[List[int], None]
            Lista de inteiros representando o conteúdo do arquivo. Retorna None se o caminho for inválido.
        """
        if not File.__check_path(path=path):
            return None

        address_array: List[int] = []
        with open(file=path, mode='rb') as file:
            while address := file.read(int(File.__address_size / 8)):
                address_array.append(int.from_bytes(address))

        return address_array

    @staticmethod
    def __check_path(path: str) -> bool:
        """
        Verifica se o caminho do arquivo é válido e se o arquivo tem extensão '.bin'.

        Parâmetros:
        -----------
        path: str
            Caminho para o arquivo.

        Retorna:
        --------
        bool
            True se o caminho for válido e o arquivo tiver extensão '.bin', False caso contrário.
        """
        return exists(path) and path.endswith('.bin')