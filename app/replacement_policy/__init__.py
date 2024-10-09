from .fifo_replacement_policy import FIFO
from .lru_replacement_policy import LRU
from .random_replacement_policy import Random
from .replacement_policy import ReplacementPolicy
from .replacement_policy_types import ReplacementPolicyType

__all__ = (
	'FIFO',
	'LRU',
	'Random',
	'ReplacementPolicyType',
	'ReplacementPolicy',
)
