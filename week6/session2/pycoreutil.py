from pathlib import Path
from typing import List

import typer

cli = typer.Typer()

# print = typer.echo

# from __future__ import print_function as print


@cli.command()
def head(file: typer.FileText, n: int = 10):
    """Print first n rows of the file"""

    lines = file.readlines()

    # for i, line in enumerate(file):
    #     typer.echo(line,nl=False)
    #     if  i  > n-1:
    #         break

    for line in lines[:n]:
        typer.echo(line, nl=False)


@cli.command()
def tail(file: typer.FileText, n: int = 10):
    """Print last n rows of the file"""
    lines = file.readlines()

    for line in lines[-n:]:
        typer.echo(line, nl=False)


def python_indicies(field: str, max_count: int) -> List[int]:
    if "-" in field:
        a, b = [int(f) for f in field.split("-")]

        lst = [i for i in range(a - 1, min(b, max_count))]
    elif "," in field:
        lst = [int(f) - 1 for f in field.split(",")]
    else:
        lst = [int(field) - 1]

    return [i for i in lst if i < max_count]


@cli.command()
def cut(file: typer.FileText, field: str, delimiter: str = "\t"):
    """Print desired fields of each line

    field:
      - integer
      - integer-integer
      - integer, integer,intger...
    """

    for line in file:
        tokens = line.split(delimiter)
        idx: List[int] = python_indicies(field, max_count=len(tokens))

        interesting_tokens = [tokens[i] for i in idx]

        typer.echo(delimiter.join(interesting_tokens))

    # 3 -> s:2, e:3 a = ['the', 'quick', 'brown', 'fox'] a[2:3]  ->[2]
    # 3-5 -> s:2, e:5 -> [2,3,4]
    # 3,5,7 -> s: [2, 4, 6]


@cli.command()
def wc(
    file: typer.FileText, character: bool = True, word: bool = True, line: bool = True
):
    """Print some statistics on file

    <line> <word> <char> <filename>
    """
    content = file.read()

    file_name = file.name

    list_of_things_to_be_printed: List[str] = []

    if line:
        linec = len(content.split("\n"))
        list_of_things_to_be_printed.append(str(linec))

    if word:
        wordc = len(content.split())
        list_of_things_to_be_printed.append(str(wordc))

    if character:
        charc = len(content)
        list_of_things_to_be_printed.append(str(charc))

    list_of_things_to_be_printed.append(file_name)

    typer.echo("    ".join(list_of_things_to_be_printed))


if __name__ == "__main__":
    cli()
