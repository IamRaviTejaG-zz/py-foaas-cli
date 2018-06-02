import click
from typing import Tuple
from fucks.fucks import Fucks

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
all_fucks = sorted(singles + doubles + triples)
a = str(', '.join(all_fucks))

@click.command()
@click.argument("fuck", nargs=-1, required=True)
def opts(fuck: Tuple) -> None:
    if (len(fuck) == 1):
        print ("Received no further arguments! List of operations:\n")
        print (a)
        exit(0)
    else:
        try:
            f = getattr(Fucks, fuck[1])
        except AttributeError:
            print ("Unexpected fuckery! List of operations:\n")
            print (a)
            exit(0)
        num_args = str(len(fuck)-2)
        if (fuck[1] in singles):
            if (len(fuck) != 3):
                print ("Expected 1 argument! Received "
                        + num_args + " argument(s).")
                exit(0)
            else:
                f(fuck[2])
        elif (fuck[1] in doubles):
            if (len(fuck) != 4):
                print ("Expected 2 arguments! Received "
                        + num_args + " argument(s).")
                exit(0)
            else:
                f(fuck[2], fuck[3])
        elif (fuck[1] in triples):
            if (len(fuck) != 5):
                print ("Expected 3 arguments! Received "
                        + num_args + " argument(s).")
                exit(0)
            else:
                f(fuck[2], fuck[3], fuck[4])
        else:
            f()

if __name__ == '__main__':
    opts()
