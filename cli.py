import click
from typing import Tuple
from fucks.fucks import Fucks

_fucks = Fucks()

singles = ["asshole", "awesome", "bag", "because", "bucket", "bye", "cool",
            "cup", "diabetes", "everyone", "everything", "family",
            "fascinating", "flying", "fyyff", "give", "horse", "immensity",
            "life", "looking", "maybe", "me", "mornin", "no", "pink",
            "programmer", "question", "retard", "ridiculous", "rtfm", "sake",
            "shit", "single", "thanks", "that", "this", "too", "tucker",
            "what", "zayn", "zero"]
doubles = ["anyway", "bday", "blackadder", "bm", "bus", "caniuse", "chainsaw",
            "cocksplat", "dalton", "deraadt", "donut", "equity", "gfy",
            "greed", "king", "keepcalm", "linus", "keep", "look", "madison",
            "nugget", "off", "offwith", "outside", "particular", "problem",
            "pulp", "shakespeare", "shutup", "think", "thinking", "thumbs",
            "xmas", "yoda", "you"]
triples = ["ballmer", "dosomething", "field"]

@click.command()
@click.argument("--option", nargs=-1, required=False)
def opts(option: Tuple) -> None:
    if (options[0] in singles):
        _fucks.options[0](options[1])
    elif (options[0] in doubles):
        _fucks.options[0](options[1], options[2])
    elif (options[0] in triples):
        _fucks.options[0](options[1], options[2], options[3])

@click.command()
@click.argument("--version", nargs=0, required=False)
def showversioninfo(version: bool) -> None:
    if (version):
        _fucks.version()

@click.command()
@click.argument("--operations", default=False, type=bool, nargs=0,
                required=False)
def showops(operations: bool) -> None:
    if (operations):
        _fucks.operations()
