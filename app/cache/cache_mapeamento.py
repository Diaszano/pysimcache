import math
import numpy as np
from app.cache.cache_policy import process_policy

class CacheMapping:
    """
    Classe para gerenciar o mapeamento de cache e calcular hits e misses.

    Attributes:
        hits (int): Número de hits na cache.
        misses (int): Número de misses na cache.
        miss_compulsory (int): Número de misses compulsórios.
        miss_capacity (int): Número de misses de capacidade.
        miss_conflict (int): Número de misses de conflito.
        cache_val (np.ndarray): Array de valores de validade da cache.
        cache_tag (np.ndarray): Array de tags da cache.
        nbits_offset (int): Número de bits para o offset.
        nbits_index (int): Número de bits para o índice.
        nbits_tag (int): Número de bits para a tag.
    """

    def __init__(
        self,
        hits: int = 0,
        misses: int = 0,
        miss_compulsory: int = 0,
        miss_capacity: int = 0,
        miss_conflict: int = 0,
    ) -> None:
        """
        Inicializa a classe CacheMapping com valores padrão.

        Args:
            hits (int): Número inicial de hits. Default é 0.
            misses (int): Número inicial de misses. Default é 0.
            miss_compulsory (int): Número inicial de misses compulsórios. Default é 0.
            miss_capacity (int): Número inicial de misses de capacidade. Default é 0.
            miss_conflict (int): Número inicial de misses de conflito. Default é 0.
        """
        self.hits = hits
        self.misses = misses
        self.miss_compulsory = miss_compulsory
        self.miss_capacity = miss_capacity
        self.miss_conflict = miss_conflict
        self.cache_val = None
        self.cache_tag = None
        self.nbits_offset = None
        self.nbits_index = None
        self.nbits_tag = None

    def initialize_cache(self, nsets, bsize, assoc):
        """
        Inicializa a cache com os parâmetros fornecidos.

        Args:
            nsets (int): Número de conjuntos na cache.
            bsize (int): Tamanho do bloco.
            assoc (int): Número de vias associativas.
        """
        self.cache_val = np.zeros(nsets * assoc)
        self.cache_tag = np.zeros(nsets * assoc)
        self.nbits_offset = int(math.log2(bsize))
        self.nbits_index = int(math.log2(nsets))
        self.nbits_tag = 32 - self.nbits_offset - self.nbits_index

    def mapping(self, memory_addresses, nsets, bsize, assoc, policy):
        """
        Realiza o mapeamento de cache para os endereços de memória fornecidos.

        Args:
            memory_addresses (list): Lista de endereços de memória.
            nsets (int): Número de conjuntos na cache.
            bsize (int): Tamanho do bloco.
            assoc (int): Número de vias associativas.
            policy (ReplacementPolicyType): Política de substituição a ser aplicada.
        """
        self.initialize_cache(nsets, bsize, assoc)
        for i in memory_addresses:
            tag = i >> (self.nbits_offset + self.nbits_index)
            index = (i >> self.nbits_offset) & (2**self.nbits_index - 1)
            if assoc == 1:
                self.mapeamento_direto(tag, index)
            elif nsets == 1:
                self.totalmente_associativa(tag, index, assoc, policy)
            else:
                self.conjunto_associativa(tag, index, nsets, assoc, policy)
        self.misses = self.miss_capacity + self.miss_conflict + self.miss_compulsory

    def mapeamento_direto(self, tag, index):
        """
        Realiza o mapeamento direto na cache.

        Args:
            tag (int): Tag do bloco.
            index (int): Índice do conjunto na cache.
        """
        if self.cache_val[index] == 0:
            self.miss_compulsory += 1
            self.cache_val[index] = 1
            self.cache_tag[index] = tag
        elif self.cache_tag[index] == tag:
            self.hits += 1
        else:
            self.cache_val[index] = 1
            self.cache_tag[index] = tag

    def totalmente_associativa(self, tag, index, assoc, policy):
        """
        Realiza o mapeamento totalmente associativo na cache.

        Args:
            tag (int): Tag do bloco.
            index (int): Índice do conjunto na cache.
            assoc (int): Número de vias associativas.
            policy (ReplacementPolicyType): Política de substituição a ser aplicada.
        """
        flag_hit, flag_compulsory = self.check_cache_mapping(tag, 0, assoc)
        if not flag_hit and not flag_compulsory:
            process_policy(assoc, policy, tag, index, self.cache_val, self.cache_tag)
            self.miss_capacity += 1  # Contabiliza miss de capacidade

    def conjunto_associativa(self, tag, index, nsets, assoc, policy):
        """
        Realiza o mapeamento conjunto associativo na cache.

        Args:
            tag (int): Tag do bloco.
            index (int): Índice do conjunto na cache.
            nsets (int): Número de conjuntos na cache.
            assoc (int): Número de vias associativas.
            policy (ReplacementPolicyType): Política de substituição a ser aplicada.
        """
        flag_hit, flag_compulsory = self.check_cache_mapping(tag, index * assoc, (index + 1) * assoc)
        cache_size = nsets * assoc
        if not flag_hit and not flag_compulsory:
            if self.miss_compulsory == cache_size:
                self.miss_capacity += 1
            else:
                self.miss_conflict += 1
            process_policy(assoc, policy, tag, index, self.cache_val, self.cache_tag)

    def check_cache_mapping(self, tag, start, end):
        """
        Verifica o mapeamento da cache para hits e misses compulsórios.

        Args:
            tag (int): Tag do bloco.
            start (int): Índice inicial do conjunto na cache.
            end (int): Índice final do conjunto na cache.

        Returns:
            tuple: Tupla contendo flags para hit e miss compulsório.
        """
        flag_hit = False
        flag_compulsory = False
        for i in range(start, end):
            if self.cache_val[i] == 0:
                flag_compulsory = True
                self.miss_compulsory += 1
                self.cache_val[i] = 1
                self.cache_tag[i] = tag
                break
            if self.cache_tag[i] == tag:
                flag_hit = True
                self.hits += 1
                break
        return flag_hit, flag_compulsory