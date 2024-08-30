from os import stat
from os.path import exists
from typing import Union, List

class File:
    """
    Classe utilitária para manipulação de arquivos, especialmente arquivos binários,
    com métodos para leitura e validação de arquivos.
    """

    @staticmethod
    def read_bin_file(path: str, address_size: int = 32) -> Union[List[int], None]:
        """
        Lê um arquivo binário e converte seu conteúdo em uma lista de endereços inteiros.

        Parâmetros:
        -----------
        path: str
            O caminho do arquivo binário a ser lido.
        address_size: int
            Tamanho de um endereço em bits

        Retorna:
        --------
        Union[List[int], None]
            Uma lista de endereços inteiros lidos do arquivo, ou None se o arquivo for inválido.

        Levanta:
        --------
        FileNotFoundError:
            Se o arquivo não for encontrado ou for inválido.
        """
        if not File.is_valid_bin_file(path=path):
            return None

        address_array: List[int] = []
        with open(file=path, mode="rb") as file:
            while address := file.read(int(address_size / 8)):
                address_array.append(int.from_bytes(address))

        return address_array

    @staticmethod
    def is_valid_file(path: str) -> bool:
        """
        Verifica se um arquivo existe e não está vazio.

        Parâmetros:
        -----------
        path: str
            O caminho do arquivo a ser verificado.

        Retorna:
        --------
        bool
            True se o arquivo existir e não estiver vazio, False caso contrário.
        """
        return exists(path=path) and not File.is_file_empty(path=path)

    @staticmethod
    def is_valid_bin_file(path: str) -> bool:
        """
        Verifica se um arquivo é um arquivo binário válido.

        Parâmetros:
        -----------
        path: str
            O caminho do arquivo a ser verificado.

        Retorna:
        --------
        bool
            True se o arquivo existir, não estiver vazio e tiver a extensão '.bin',
            False caso contrário.
        """
        return File.is_valid_file(path=path) and path.endswith(".bin")

    @staticmethod
    def is_file_empty(path: str) -> bool:
        """
        Verifica se um arquivo está vazio.

        Parâmetros:
        -----------
        path: str
            O caminho do arquivo a ser verificado.

        Retorna:
        --------
        bool
            True se o arquivo estiver vazio, False caso contrário.

        Levanta:
        --------
        FileNotFoundError:
            Se o arquivo não existir.
        """
        return stat(path=path).st_size == 0
