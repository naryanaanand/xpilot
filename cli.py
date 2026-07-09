import typer

from rich.console import Console

from commands.test import app as test_app

app = typer.Typer()

console = Console()

app.add_typer(
    test_app,
    name="test"
)
