import os
import sys

try:
    import rich
except ImportError:
    rich = None
else:
    from rich.console import Console

from . import __doc__, __path__
from .words import words

if rich:
    console = Console()

if "--help" in sys.argv:
    print(__doc__)
if len(sys.argv) > 1:
    starting_letters = sys.argv[1]
    matched_words = enumerate([word for word in words if word.startswith(starting_letters)], 1)
    if rich:
        rich.print(
            "\n".join(
                f"{n}. [underline]{starting_letters}[/underline]{word.replace(starting_letters, '')}"
                for n, word in matched_words
            )
        )
    else:
        print("\n".join(f"{n}. {word}" for n, word in matched_words if word.startswith(starting_letters)))
else:
    while True:
        try:
            if rich:
                starting_letters = console.input("[green]What letters does it start with?[/green]\n")
            else:
                starting_letters = input("What letters does it start with?\n")
        except KeyboardInterrupt:
            rich.print("[red]Bye![/red]") if rich else print("Bye!")
            break
        matched_words = enumerate([word for word in words if word.startswith(starting_letters)], 1)
        if rich:
            rich.print(
                "\n".join(
                    f"{n}. [underline]{starting_letters}[/underline]{word.replace(starting_letters, '')}"
                    for n, word in matched_words
                )
            )
        else:
            print("\n".join(f"{n}. {word}" for n, word in matched_words if word.startswith(starting_letters)))
        if rich:
            rich.print("[yellow]Waiting for another word, Press Ctrl+C to quit[/yellow]")
        else:
            print("[yellow]Waiting for another word, Press Ctrl+C to quit[/yellow]")


def run():
    pass
