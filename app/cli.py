import argparse
import sys
import os
import numpy as np
import math

from typer import Argument, Typer
from typing_extensions import Annotated
from .replacement_policy import ReplacementPolicyType

app = Typer()

@app.command()
def simular_cache(
		# Inputs do usuário
		nsets: Annotated[int, Argument(min=0)],
		bsize: Annotated[int, Argument(min=0)],
		assoc: Annotated[int, Argument(min=0)],
		policy: ReplacementPolicyType,
		output: Annotated[int, Argument(min=0, max=1)],
		arquivo: str,
) -> None:
	# Inicializando os contadores
	hits = 0
	misses = 0
	miss_compulsorio = 0
	miss_capacidade = 0
	miss_conflito = 0

	# Código principal da função simular_cache
	exibir_parametros(nsets, bsize, assoc, policy, output, arquivo) # TIRAR DEPOIS
	enderecos = enderecamento(arquivo)

	nbits_offset = int(math.log2(bsize))
	nbits_indice = int(math.log2(nsets))
	nbits_tag = 32 - nbits_offset - nbits_indice

	cache_val = np.zeros(nsets * assoc)
	cache_tag = np.zeros(nsets * assoc)

	if assoc == 1:
		for i in enderecos:
			tag = i >> (nbits_offset + nbits_indice)
			indice = (i >> nbits_offset) & (2 ** nbits_indice - 1)

			if cache_val[indice] == 0:
				miss_compulsorio += 1
				cache_val[indice] = 1
				cache_tag[indice] = tag

			else:
				if cache_tag[indice] == tag:
					hits += 1
				else:
					misses += 1
					cache_val[indice] = 1
					cache_tag[indice] = tag

	misses = miss_capacidade + miss_conflito + miss_compulsorio

	if output == 0:
		# Impressão formal = 0
		print(f"\nacessos: {hits + misses}" +
		f"\nhits: {hits/100}" +
		f"\nmisses: {misses/100}" +
		f"\nmiss_compulsorio: {miss_compulsorio/misses:.2f}" +
		f"\nmiss_capacidade: {miss_capacidade/misses:.2f}" +
		f"\nmiss_conflito: {miss_conflito/misses:.2f}")

	elif output == 1:
		# Impressão informal = 1
		print(f"\n{hits + misses}" +
			  f" {hits/100}" +
			  f" {misses/100}" +
			  f" {miss_compulsorio/misses:.2f}" +
			  f" {miss_capacidade/misses:.2f}" +
			  f" {miss_conflito/misses:.2f}")

# Aceitar input somente se tiver 'cache_simulator' como primeiro argumento (precisa estar nessa parte do codigo por algum motivo)
if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('command', help='The command to run')
	args, unknown = parser.parse_known_args()

	if args.command != 'cache_simulator':
		print("Erro: O primeiro argumento precisa ser 'cache_simulator'")
		sys.exit(1)

	sys.argv = sys.argv[1:]

def exibir_parametros(nsets, bsize, assoc, policy, output, arquivo) -> None:
	print(f"nsets: {nsets}")
	print(f"bsize: {bsize}")
	print(f"assoc: {assoc}")
	print(f"policy: {policy}")
	print(f"output: {output}")
	print(f"file: {arquivo}")

def enderecamento(file_name, directory="address"):
	file_path = os.path.join(directory, file_name)
	file_ext = os.path.splitext(file_path)[1]

	if os.path.exists(file_path):
		try:
			enderecos = []

			if file_ext == '.bin':
				with open(file_path, 'rb') as file:
					while True:
						bytes_lidos = file.read(4)
						if not bytes_lidos:
							break
						endereco = int.from_bytes(bytes_lidos, 'big')
						enderecos.append(endereco)

			elif file_ext == '.txt':
				with open(file_path, 'r', encoding='utf-8') as file:
					for line in file:
						endereco = int(line.strip())
						enderecos.append(endereco)

			else:
				return f"Formato de arquivo não suportado: {file_ext}"

			return enderecos

		except Exception as e:
			return f"Ocorreu um erro ao abrir ou processar o arquivo: {e}"
	else:
		return f"O arquivo {file_name} não foi encontrado no diretório {directory}."

app()
