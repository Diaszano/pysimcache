from app.cache import Block
from app.replacement_policy import Random, LRU, FIFO, ReplacementPolicyType

def process_policy(assoc, policy, tag, indice, cache_val, cache_tag):
    # Cria uma lista de blocos a partir dos valores da cache para o conjunto específico
    blocks = [
        Block(valid=bool(cache_val[indice * assoc + j]), tag=cache_tag[indice * assoc + j]) for j in range(assoc)
    ]
    # Cria um novo bloco com a tag fornecida
    new_block = Block(valid=True, tag=tag)

    # Mapeia as políticas de substituição às suas respectivas funções
    policy_map = {
        ReplacementPolicyType.RANDOM: Random.add,
        ReplacementPolicyType.FIFO: FIFO.add,
        ReplacementPolicyType.LRU: LRU.add
    }

    # Aplica a política de substituição
    updated_blocks = policy_map[policy](blocks, new_block)

    # Atualiza os valores da cache com os blocos atualizados para o conjunto específico
    for j in range(assoc):
        idx = indice * assoc + j
        cache_val[idx] = 1 if updated_blocks[j].valid else 0
        cache_tag[idx] = updated_blocks[j].tag if updated_blocks[j].valid else cache_tag[idx]

    return cache_val, cache_tag