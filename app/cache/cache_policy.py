from app.cache import Block
from app.replacement_policy import Random


def process_random_policy(assoc, tag, cache_val, cache_tag):
    # Cria uma lista de blocos a partir dos valores da cache
    blocks = [Block(valid=bool(cache_val[j]), tag=cache_tag[j]) for j in range(assoc)]
    # Cria um novo bloco com a tag fornecida
    new_block = Block(valid=True, tag=tag)
    # Aplica a política de substituição Random
    updated_blocks = Random.add(blocks, new_block)
    # Atualiza os valores da cache com os blocos atualizados
    for j in range(assoc):
        cache_val[j] = 1 if updated_blocks[j].valid else 0
        cache_tag[j] = updated_blocks[j].tag if updated_blocks[j].valid else cache_tag[j]

    return cache_val, cache_tag