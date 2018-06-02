import requests
from sys import stdout

def makerequest(*args) -> None:
    baseUrl = "http://foaas.com/"
    url = ""
    if (len(args) == 1):
        url = baseUrl + args[0]
    elif (len(args) == 2):
        url = baseUrl + args[0] + '/' + args[1]
    elif (len(args) == 3):
        url = baseUrl + args[0] + '/' + args[1] + '/' + args[2]
    elif (len(args) == 4):
        url = baseUrl + args[0] + '/' + args[1] + '/' + args[2] + '/' + args[3]
    headers = {'Accept': 'text/plain'}
    r = requests.get(url, headers=headers)
    s = str(r.content)[2:len(str(r.content))-1]
    stdout.write ('\n' + s + '\n')

class Fucks:
    def version() -> None:
        makerequest("version")

    def operations() -> None:
        makerequest("operations")

    def anyway(company: str, from_name: str) -> None:
        makerequest("anyway", company, from_name)

    def asshole(from_name: str) -> None:
        makerequest("asshole", from_name)

    def awesome(from_name: str) -> None:
        makerequest("awesome", from_name)

    def back(name: str, from_name: str) -> None:
        makerequest("back", name, from_name)

    def bag(from_name: str) -> None:
        makerequest("bag", from_name)

    def ballmer(name: str, company: str, from_name: str) -> None:
        makerequest("ballmer", name, company, from_name)

    def bday(name: str, from_name: str) -> None:
        makerequest("bday", name, from_name)

    def because(from_name: str) -> None:
        makerequest("because", from_name)

    def blackadder(name: str, from_name: str) -> None:
        makerequest("blackadder", name, from_name)

    def bm(name: str, from_name: str) -> None:
        makerequest("bm", name, from_name)

    def bucket(from_name: str) -> None:
        makerequest("bucket", from_name)

    def bus(name: str, from_name: str) -> None:
        makerequest("bus", name, from_name)

    def bye(from_name: str) -> None:
        makerequest("bye", from_name)

    def caniuse(tool: str, from_name: str) -> None:
        makerequest("caniuse", tool, from_name)

    def chainsaw(name: str, from_name: str) -> None:
        makerequest("chainsaw", name, from_name)

    def cocksplat(name: str, from_name: str) -> None:
        makerequest("cocksplat", name, from_name)

    def cool(from_name: str) -> None:
        makerequest("bye", from_name)

    def cup(from_name: str) -> None:
        makerequest("bye", from_name)

    def dalton(name: str, from_name: str) -> None:
        makerequest("dalton", name, from_name)

    def deraadt(name: str, from_name: str) -> None:
        makerequest("deraadt", name, from_name)

    def diabetes(from_name: str) -> None:
        makerequest("diabetes", from_name)

    def donut(name: str, from_name: str) -> None:
        makerequest("donut", name, from_name)

    def dosomething(do: str, something: str,
                    from_name: str) -> None:
        makerequest("dosomething", do, something, from_name)

    def equity(name: str, from_name: str) -> None:
        makerequest("equity", name, from_name)

    def everyone(from_name: str) -> None:
        makerequest("everyone", from_name)

    def everything(from_name: str) -> None:
        makerequest("everthing", from_name)

    def family(from_name: str) -> None:
        makerequest("family", from_name)

    def fascinating(from_name: str) -> None:
        makerequest("fascinating", from_name)

    def field(name: str, from_name: str, reference: str) -> None:
        makerequest("field", name, from_name, reference)

    def flying(from_name: str) -> None:
        makerequest("flying", from_name)

    def fyyff(from_name: str) -> None:
        makerequest("fyyff", from_name)

    def gfy(name: str, from_name: str) -> None:
        makerequest("gfy", name, from_name)

    def give(from_name: str) -> None:
        makerequest("give", from_name)

    def greed(noun: str, from_name: str) -> None:
        makerequest("greed", noun, from_name)

    def horse(from_name: str) -> None:
        makerequest("horse", from_name)

    def immensity(from_name: str) -> None:
        makerequest("immensity", from_name)

    def ing(name: str, from_name: str) -> None:
        makerequest("ing", name, from_name)

    def life(from_name: str) -> None:
        makerequest("life", from_name)

    def keep(name: str, from_name: str) -> None:
        makerequest("keep", name, from_name)

    def keepcalm(reaction: str, from_name: str) -> None:
        makerequest("keepcalm", reaction, from_name)

    def king(name: str, from_name: str) -> None:
        makerequest("king", name, from_name)

    def linus(name: str, from_name: str) -> None:
        makerequest("linus", name, from_name)

    def look(name: str, from_name: str) -> None:
        makerequest("look", name, from_name)

    def looking(from_name: str) -> None:
        makerequest("looking", from_name)

    def madison(name: str, from_name: str) -> None:
        makerequest("madison", name, from_name)

    def maybe(from_name: str) -> None:
        makerequest("maybe", from_name)

    def me(from_name: str) -> None:
        makerequest("me", from_name)

    def mornin(from_name: str) -> None:
        makerequest("mornin", from_name)

    def no(from_name: str) -> None:
        makerequest("no", from_name)

    def nugget(name: str, from_name: str) -> None:
        makerequest("nugget", name, from_name)

    def off(name: str, from_name: str) -> None:
        makerequest("off", name, from_name)

    def offwith(behavior: str, from_name: str) -> None:
        makerequest("off-with", behavior, from_name)

    def outside(name: str, from_name: str) -> None:
        makerequest("outside", name, from_name)

    def particular(thing: str, from_name: str) -> None:
        makerequest("particular", thing, from_name)

    def pink(from_name: str) -> None:
        makerequest("pink", from_name)

    def problem(name: str, from_name: str) -> None:
        makerequest("problem", name, from_name)

    def programmer(from_name: str) -> None:
        makerequest("programmer", from_name)

    def pulp(name: str, from_name: str) -> None:
        makerequest("pulp", name, from_name)

    def question(from_name: str) -> None:
        makerequest("question", from_name)

    def retard(from_name: str) -> None:
        makerequest("retard", from_name)

    def ridiculous(from_name: str) -> None:
        makerequest("ridiculous", from_name)

    def rtfm(from_name: str) -> None:
        makerequest("rtfm", from_name)

    def sake(from_name: str) -> None:
        makerequest("sake", from_name)

    def shakespeare(name: str, from_name: str) -> None:
        makerequest("shakespeare", name, from_name)

    def shit(from_name: str) -> None:
        makerequest("shit", from_name)

    def shutup(name: str, from_name: str) -> None:
        makerequest("shutup", name, from_name)

    def single(from_name: str) -> None:
        makerequest("single", from_name)

    def thanks(from_name: str) -> None:
        makerequest("thanks", from_name)

    def that(from_name: str) -> None:
        makerequest("that", from_name)

    def think(name: str, from_name: str) -> None:
        makerequest("think", name, from_name)

    def thinking(name: str, from_name: str) -> None:
        makerequest("thinking", name, from_name)

    def this(from_name: str) -> None:
        makerequest("this", from_name)

    def thumbs(name: str, from_name: str) -> None:
        makerequest("thumbs", name, from_name)

    def too(from_name: str) -> None:
        makerequest("too", from_name)

    def tucker(from_name: str) -> None:
        makerequest("tucker", from_name)

    def what(from_name: str) -> None:
        makerequest("what", from_name)

    def xmas(name: str, from_name: str) -> None:
        makerequest("xmas", name, from_name)

    def yoda(name: str, from_name: str) -> None:
        makerequest("yoda", name, from_name)

    def you(name: str, from_name: str) -> None:
        makerequest("you", name, from_name)

    def zayn(from_name: str) -> None:
        makerequest("zayn", from_name)

    def zero(from_name: str) -> None:
        makerequest("zero", from_name)
