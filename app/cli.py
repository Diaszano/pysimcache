from typer import Argument, Typer
from typing_extensions import Annotated

from .cache import Mapeamentos
from .file import File
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

	# Código principal da função simular_cache
	exibir_parametros(
		nsets, bsize, assoc, policy, output, arquivo
	)  # TIRAR DEPOIS

	enderecos = File.read_bin_file('address/' + arquivo)
	# print(enderecos)

	cache = Mapeamentos()
	cache.mapeamento(enderecos, nsets, bsize, assoc, policy)

	exibir_resultados(
		cache.hits,
		cache.misses,
		cache.miss_compulsorio,
		cache.miss_capacidade,
		cache.miss_conflito,
		output,
	)


def exibir_parametros(nsets, bsize, assoc, policy, output, arquivo) -> None:
	print(
		f'nsets: {nsets}\n'
		+ f'bsize: {bsize}\n'
		+ f'assoc: {assoc}\n'
		+ f'policy: {policy}\n'
		+ f'output: {output}\n'
		+ f'file: {arquivo}\n'
	)


def exibir_resultados(
	hits, misses, miss_compulsorio, miss_capacidade, miss_conflito, output
) -> None:
	if output == 0:
		# Impressão formal = 0
		print(
			f'\nacessos: {hits + misses}'
			+ f'\nhits: {hits} | {(hits/(hits + misses))*100:.2f}%'
			+ f'\nmisses: {misses} | {(misses/(hits + misses))*100:.2f}%'
			+ f'\nmiss_compulsorio: {miss_compulsorio} | {(miss_compulsorio/misses)*100:.2f}%'
			+ f'\nmiss_capacidade: {miss_capacidade} | {(miss_capacidade/misses)*100:.2f}%'
			+ f'\nmiss_conflito: {miss_conflito} | {(miss_conflito/misses)*100:.2f}%'
		)

	elif output == 1:
		# Impressão informal = 1
		print(
			f'\n{hits + misses}'
			+ f' {hits/(hits + misses):.4f}'
			+ f' {misses/(hits + misses):.4f}'
			+ f' {miss_compulsorio/misses:.2f}'
			+ f' {miss_capacidade/misses:.2f}'
			+ f' {miss_conflito/misses:.2f}'
		)


app()
