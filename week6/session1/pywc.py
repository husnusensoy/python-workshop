#!/Users/husnusensoy/miniconda39/envs/python-training38/bin/python

from pathlib import Path

import typer

wc = typer.Typer()


def char_count(content: str) -> int:
    
    
    return len(content)


def word_count(content: str) -> int:



    return len(content.split())


def line_count(content: str) -> int:
    lines = content.splitlines()

    return len(lines)


@wc.command()
def cmd(
    path: Path = typer.Option(..., exists=True,readable=True,dir_okay=False),
    char: bool = True,
    word: bool = True,
    line: bool = True,
):
    """Echos some statistics on file

    <line> <word> <char> <filename>
    """

    tokens = []
    content = path.read_text()
    if line:
        l = line_count(content)
        tokens.append(str(l))

    if word:
        w = word_count(content)
        tokens.append(str(w))

    if char:
        c = char_count(content)
        tokens.append(str(c))
        tokens.append(path.name)

        typer.echo(f'{"    ".join(tokens)}')


if __name__ == "__main__":
    wc()
