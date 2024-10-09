from enum import Enum


class OutputType(str, Enum):
	"""
	Enumeração que define os tipos de saída para a simulação de cache.

	- FREE: Saída livre ou personalizada.
	- STANDARD: Saída padrão, com informações mínimas.
	"""

	FREE = '0'
	STANDARD = '1'
