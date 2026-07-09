from cli import app
from rich.console import Console

console = Console()


@app.callback(invoke_without_command=True)
def root():

    console.print()

    console.print("[bold cyan]XPilot[/bold cyan]")

    console.print("[green]AI Content Operating System[/green]")

    console.print()

    console.print("Available commands:")

    console.print("  research")

    console.print("  github")

    console.print("  reddit")

    console.print("  tweet")

    console.print("  thread")

    console.print("  critique")

    console.print("  history")

    console.print("  copy")

    console.print()


if __name__ == "__main__":
    app()
