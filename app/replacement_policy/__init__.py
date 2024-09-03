from .fifo_replacement_policy import FIFOReplacementPolicy
from .lru_replacement_policy import LRUReplacementPolicy
from .random_replacement_policy import RandomReplacementPolicy
from .replacement_policy_types import ReplacementPolicyType

__all__ = (
	'FIFOReplacementPolicy',
	'LRUReplacementPolicy',
	'RandomReplacementPolicy',
	'ReplacementPolicyType',
)
