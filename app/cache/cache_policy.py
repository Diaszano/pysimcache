from app.cache import Block
from app.replacement_policy import FIFO, LRU, Random, ReplacementPolicyType

def process_policy(assoc, policy, tag, index, cache_val, cache_tag):
    """
    Processa a política de substituição de cache.

    Args:
        assoc (int): Número de vias associativas.
        policy (ReplacementPolicyType): Política de substituição a ser aplicada.
        tag (int): Tag do novo bloco.
        index (int): Índice do conjunto na cache.
        cache_val (list): Lista de valores de validade da cache.
        cache_tag (list): Lista de tags da cache.

    Returns:
        tuple: Tupla contendo as listas atualizadas de valores de validade e tags da cache.
    """
    blocks = create_blocks(assoc, index, cache_val, cache_tag)
    new_block = Block(valid=True, tag=tag)
    updated_blocks = select_policy(policy, blocks, new_block)
    update_cache_values(assoc, index, updated_blocks, cache_val, cache_tag)
    return cache_val, cache_tag

def create_blocks(assoc, index, cache_val, cache_tag):
    """
    Cria uma lista de blocos a partir dos valores da cache para o conjunto específico.

    Args:
        assoc (int): Número de vias associativas.
        index (int): Índice do conjunto na cache.
        cache_val (list): Lista de valores de validade da cache.
        cache_tag (list): Lista de tags da cache.

    Returns:
        list: Lista de blocos do conjunto específico.
    """
    return [
        Block(
            valid=bool(cache_val[index * assoc + j]),
            tag=cache_tag[index * assoc + j],
        )
        for j in range(assoc)
    ]

def select_policy(policy, blocks, new_block):
    """
    Seleciona e aplica a política de substituição de cache.

    Args:
        policy (ReplacementPolicyType): Política de substituição a ser aplicada.
        blocks (list): Lista de blocos existentes no conjunto.
        new_block (Block): Novo bloco a ser adicionado.

    Returns:
        list: Lista de blocos atualizada após a aplicação da política de substituição.
    """
    if policy == ReplacementPolicyType.RANDOM:
        return Random.add(blocks, new_block)
    if policy == ReplacementPolicyType.FIFO:
        return FIFO.add(blocks, new_block)
    if policy == ReplacementPolicyType.LRU:
        return LRU.add(blocks, new_block)
    return blocks

def update_cache_values(assoc, index, updated_blocks, cache_val, cache_tag):
    """
    Atualiza os valores da cache com os blocos atualizados para o conjunto específico.

    Args:
        assoc (int): Número de vias associativas.
        index (int): Índice do conjunto na cache.
        updated_blocks (list): Lista de blocos atualizada.
        cache_val (list): Lista de valores de validade da cache.
        cache_tag (list): Lista de tags da cache.
    """
    for j in range(assoc):
        cache_val[index * assoc + j] = 1 if updated_blocks[j].valid else 0
        cache_tag[index * assoc + j] = (
            updated_blocks[j].tag
            if updated_blocks[j].valid
            else cache_tag[index * assoc + j]
        )