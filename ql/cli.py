from rich.console import Console
from rich.panel import Panel
import click
from ql.commands import init

console = Console()

@click.group()
def main():
    """Quickline CLI"""
    console.print(
        Panel(
            "Quickline CLI",
            title="Quickline",
            border_style="bold cyan"
        )
    )
    pass

# Register commands
main.add_command(init.init_cmd)