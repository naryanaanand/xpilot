import typer

from rich.console import Console

from commands.research import app as research_app

app = typer.Typer(
    help="XPilot CLI"
)

console = Console()

app.add_typer(
    research_app,
    name="research",
)
