from logging import CRITICAL, DEBUG, basicConfig
from pathlib import Path

from typer import Argument, Typer
from typing_extensions import Annotated

from .cache import Mapping
from .file import File
from .replacement_policy import FIFO, LRU, Random, ReplacementPolicyType
from .tools import Output, OutputType

app = Typer()


@app.command()
def main(
	nsets: Annotated[int, Argument(min=0)],
	bsize: Annotated[int, Argument(min=0)],
	assoc: Annotated[int, Argument(min=0)],
	policy: ReplacementPolicyType,
	output: OutputType,
	file_name: str,
) -> None:
	"""
	Função principal que executa a simulação do mapeamento de cache.

	:param nsets: Número de conjuntos (sets) no cache.
	:param bsize: Tamanho do bloco de cache em bytes.
	:param assoc: Grau de associatividade do cache.
	:param policy: Tipo da política de substituição (FIFO, LRU, Random).
	:param output: Tipo de saída (padrão, detalhada ou em arquivo).
	:param file_name: Nome do arquivo binário contendo os endereços de memória.
	:raises FileNotFoundError: Se o arquivo de endereços binário não for encontrado.
	"""  # noqa: E501
	level_log = CRITICAL if output == OutputType.STANDARD else DEBUG
	basicConfig(
		filename='pysimcache.log',
		format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
		level=level_log,
	)
	Output.parameters(nsets, bsize, assoc, policy, file_name, output)

	if not File.is_valid_bin_file(file_name):
		tmp = Path('address').joinpath(file_name)
		if not File.is_valid_bin_file(tmp.__str__()):
			raise FileNotFoundError('O arquivo %s não existe!' % file_name)
		file_name = tmp.__str__()

	match policy:
		case ReplacementPolicyType.RANDOM:
			policy = Random
		case ReplacementPolicyType.FIFO:
			policy = FIFO
		case ReplacementPolicyType.LRU:
			policy = LRU

	addresses = File.read_bin_file(file_name)

	cache = Mapping(nsets=nsets, bsize=bsize, assoc=assoc, policy=policy)

	hits, misses, miss_compulsory, miss_capacity, miss_conflict = cache.mapping(
		addresses
	)

	Output.results(
		hits, misses, miss_compulsory, miss_capacity, miss_conflict, output
	)


app()
