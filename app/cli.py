from typer import Argument, Typer
from typing_extensions import Annotated

from .replacement_policy import ReplacementPolicyType

app = Typer()


@app.command()
def main(
	nsets: Annotated[int, Argument(min=0)],
	bsize: Annotated[int, Argument(min=0)],
	assoc: Annotated[int, Argument(min=0)],
	policy: ReplacementPolicyType,
	output: Annotated[int, Argument(min=0, max=1)],
	file: str,
) -> None:
	pass


app()
