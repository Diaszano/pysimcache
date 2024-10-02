from enum import Enum


class ReplacementPolicyType(str, Enum):
	"""Enumeração que define os tipos de políticas de substituição de cache.

	Cada valor enum representa um tipo de política de substituição:
		- 'R' para substituição aleatória (Random Replacement).
		- 'F' para substituição FIFO (First-In, First-Out).
		- 'L' para substituição LRU (Least Recently Used).
	"""

	RANDOM = 'R'
	FIFO = 'F'
	LRU = 'L'
