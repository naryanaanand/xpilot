
import typer

from rich import print

from tools.openai_client import OpenAIClient

app = typer.Typer()


@app.command()
def test():

    client = OpenAIClient()

    answer = client.generate(

        "Say hello in one sentence."

    )

    print(answer)import typer

from rich import print

from tools.openai_client import OpenAIClient

app = typer.Typer()


@app.command()
def test():

    client = OpenAIClient()

    answer = client.generate(

        "Say hello in one sentence."

    )

    print(answer)
