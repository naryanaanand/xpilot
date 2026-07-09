import typer

from rich.console import Console

from tools.llm import LLM

console = Console()

app = typer.Typer()


@app.command()
def research():

    console.print()

    console.print("[cyan]Research Agent[/cyan]")

    console.print()

    llm = LLM()

    answer = llm.generate(
        prompt="Tell me one interesting AI development today in under 120 words."
    )

    console.print(answer)

    console.print()
