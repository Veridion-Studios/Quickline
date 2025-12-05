from rich.console import Console
from rich.panel import Panel
from rich.align import Align
import click

@click.command(name="about")
def about_cmd():
    """Display information about Quickline."""
    console = Console()
    console.print(
        Panel(
            Align.left(
                "[bold]Quickline[/bold] is a modern CLI tool built for developers.\n"
                "It allows you to scaffold projects for your favorite frameworks, including NextJS, React, Vite, and more.\n"
                "• 🚀 Fast\n"
                "• 🛠️ Easy to use\n"
                "• 🎨 Beautiful output\n"
                "• 📦 Supports multiple frameworks\n"
                "\n[blue]GitHub (ctrl + click):[/blue] https://github.com/Veridion-Studios/Quickline\n"
                "\n[dim]Quickline is developed and maintained by TheAwesomeAJ, and is part of the Veridion Studios ecosystem.[/dim]"
            ),
            border_style="bold green"
        ),
        markup=True
    )