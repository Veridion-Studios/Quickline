from rich.console import Console
from rich.panel import Panel
import click

@click.command(name="init")
def init_cmd():
    """Initialize a Quickline project."""
    console = Console()
    console.print(
        Panel(
            "[green]Quickline is initialized![/green]",
            title="Success",
            border_style="bold green"
        )
    )