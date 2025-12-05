from rich.console import Console
from rich.panel import Panel
import click
from click_help_colors import HelpColorsGroup, HelpColorsCommand
from ql.commands import about, init
import time

console = Console()

# with console.status("[bold cyan]Loading...[/bold cyan]", spinner="dots"):
#    time.sleep(3)

@click.group(
    cls=HelpColorsGroup,
    help_headers_color='cyan',
    help_options_color='magenta',
    help_options_custom_colors={'--help': 'green'}
)
def main():
    """Quickline CLI"""
    console.print(
        Panel(
            "[bold cyan]Quickline CLI[/bold cyan]",
            title="Quickline",
            border_style="bold cyan"
        )
    )

main.add_command(init.init_cmd)
main.add_command(about.about_cmd)