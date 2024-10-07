import math

import numpy as np

from app.cache.cache_policy import process_policy


class Mapeamentos:
	def __init__(
		self,
		hits: int = 0,
		misses: int = 0,
		miss_compulsorio: int = 0,
		miss_capacidade: int = 0,
		miss_conflito: int = 0,
	) -> None:
		# Valores para a impressão
		self.hits = hits
		self.misses = misses
		self.miss_compulsorio = miss_compulsorio
		self.miss_capacidade = miss_capacidade
		self.miss_conflito = miss_conflito
		# Valores para trabalhar a cache
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

	def mapeamento(self, enderecos, nsets, bsize, assoc, policy):
		self.valores(nsets, bsize, assoc)

		for i in enderecos:
			tag = i >> (self.nbits_offset + self.nbits_indice)
			indice = (i >> self.nbits_offset) & (2**self.nbits_indice - 1)

			if assoc == 1:
				self.mapeamento_direto(tag, indice)
			elif nsets == 1:
				self.totalmente_associativa(tag, indice, assoc, policy)
			else:
				self.conjunto_associativa(tag, indice, nsets, assoc, policy)

		self.misses = (
			self.miss_capacidade + self.miss_conflito + self.miss_compulsorio
		)

	def mapeamento_direto(self, tag, indice):
		if self.cache_val[indice] == 0:
			self.miss_compulsorio += 1
			self.cache_val[indice] = 1
			self.cache_tag[indice] = tag
		elif self.cache_tag[indice] == tag:
			self.hits += 1
		else:
			self.cache_val[indice] = 1
			self.cache_tag[indice] = tag

	def totalmente_associativa(self, tag, indice, assoc, policy):
		flag_hit = False
		flag_compulsorio = False

		for i in range(assoc):
			if self.cache_val[i] == 0:
				flag_compulsorio = True
				self.miss_compulsorio += 1
				self.cache_val[i] = 1
				self.cache_tag[i] = tag
				break
			if self.cache_tag[i] == tag:
				flag_hit = True
				self.hits += 1
				break

		if not flag_hit and not flag_compulsorio:
			process_policy(assoc, policy, tag, indice, self.cache_val, self.cache_tag)
			self.miss_capacidade += 1  # Contabiliza miss de capacidade
			self.misses += 1

	def conjunto_associativa(self, tag, indice, nsets, assoc, policy):
		flag_hit = False
		flag_compulsorio = False
		tamanho_cache = assoc * nsets
		for i in range(indice * assoc, (indice * assoc) + assoc):
			if self.cache_val[i] == 0:
				flag_compulsorio = True
				self.miss_compulsorio += 1
				self.cache_val[i] = 1
				self.cache_tag[i] = tag
				break
			if self.cache_tag[i] == tag:
				flag_hit = True
				self.hits += 1
				break

		if not flag_hit and not flag_compulsorio:
			if self.miss_compulsorio == tamanho_cache:
				self.miss_capacidade += 1
			else:
				self.miss_conflito += 1

			process_policy(assoc, policy, tag, indice, self.cache_val, self.cache_tag)
