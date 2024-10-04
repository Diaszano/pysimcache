import numpy as np
import math

class Mapeamentos:
    def __init__(self, hits: int = 0, misses: int = 0, miss_compulsorio: int = 0, miss_capacidade: int = 0, miss_conflito: int = 0) -> None:
        self.hits = hits
        self.misses = misses
        self.miss_compulsorio = miss_compulsorio
        self.miss_capacidade = miss_capacidade
        self.miss_conflito = miss_conflito
        self.cache_val = None
        self.cache_tag = None
        self.nbits_offset = None
        self.nbits_indice = None
        self.nbits_tag = None

    def valores(self, nsets, bsize, assoc):
        self.cache_val = np.zeros(nsets * assoc)
        self.cache_tag = np.zeros(nsets * assoc)

        self.nbits_offset = int(math.log2(bsize))
        self.nbits_indice = int(math.log2(nsets))
        self.nbits_tag = 32 - self.nbits_offset - self.nbits_indice

    def mapeamento_direto(self, enderecos):
        for i in enderecos:
            tag = i >> (self.nbits_offset + self.nbits_indice)
            indice = (i >> self.nbits_offset) & (2 ** self.nbits_indice - 1)

            if self.cache_val[indice] == 0:
                self.miss_compulsorio += 1
                self.cache_val[indice] = 1
                self.cache_tag[indice] = tag
            else:
                if self.cache_tag[indice] == tag:
                    self.hits += 1
                else:
                    self.misses += 1
                    self.cache_val[indice] = 1
                    self.cache_tag[indice] = tag

        self.misses = self.miss_capacidade + self.miss_conflito + self.miss_compulsorio