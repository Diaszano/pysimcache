from app.cache import Block
from .cache_set import Set
from app.replacement_policy import ReplacementPolicyType

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
    cache_set = create_set(assoc, index, cache_val, cache_tag, policy)
    new_block = Block(valid=True, tag=tag)
    cache_set.add_block(new_block)
    update_cache_values(assoc, index, cache_set.get_blocks(), cache_val, cache_tag)
    return cache_val, cache_tag

def create_set(assoc, index, cache_val, cache_tag, policy):
    """
    Cria um conjunto de blocos a partir dos valores da cache para o conjunto específico.

    Args:
        assoc (int): Número de vias associativas.
        index (int): Índice do conjunto na cache.
        cache_val (list): Lista de valores de validade da cache.
        cache_tag (list): Lista de tags da cache.
        policy (ReplacementPolicyType): Política de substituição a ser aplicada.

    Returns:
        Set: Conjunto de blocos do conjunto específico.
    """
    # Cria o conjunto usando a política diretamente
    cache_set = Set(assoc, policy)
    blocks = [
        Block(
            valid=bool(cache_val[index * assoc + j]),
            tag=cache_tag[index * assoc + j],
        )
        for j in range(assoc)
    ]
    for block in blocks:
        cache_set.add_block(block)
    return cache_set

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
