import requests

def printresult(a: str) -> None:
    print (a)

def makerequest(*args) -> None:
    baseUrl = "http://foaas.com/"
    url = ""
    print (len(args))
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
    printresult(s)

class Fucks:
    def __init__(self):
        pass

    def version(self: None) -> None:
        makerequest("version")

    def operations(self: None) -> None:
        makerequest("operations")

    def anyway(self: None, company: str, from_name: str) -> None:
        makerequest("anyway", company, from_name)

    def asshole(self: None, from_name: str) -> None:
        makerequest("asshole", from_name)

    def awesome(self: None, from_name: str) -> None:
        makerequest("awesome", from_name)

    def back(self: None, name: str, from_name: str) -> None:
        makerequest("back", name, from_name)

    def bag(self: None, from_name: str) -> None:
        makerequest("bag", from_name)

    def ballmer(self: None, name: str, company: str, from_name: str) -> None:
        makerequest("ballmer", name, company, from_name)

    def bday(self: None, name: str, from_name: str) -> None:
        makerequest("bday", name, from_name)

    def because(self: None, from_name: str) -> None:
        makerequest("because", from_name)

    def blackadder(self: None, name: str, from_name: str) -> None:
        makerequest("blackadder", name, from_name)

    def bm(self: None, name: str, from_name: str) -> None:
        makerequest("bm", name, from_name)

    def bucket(self: None, from_name: str) -> None:
        makerequest("bucket", from_name)

    def bus(self: None, name: str, from_name: str) -> None:
        makerequest("bus", name, from_name)

    def bye(self: None, from_name: str) -> None:
        makerequest("bye", from_name)

    def caniuse(self: None, tool: str, from_name: str) -> None:
        makerequest("caniuse", tool, from_name)

    def chainsaw(self: None, name: str, from_name: str) -> None:
        makerequest("chainsaw", name, from_name)

    def cocksplat(self: None, name: str, from_name: str) -> None:
        makerequest("cocksplat", name, from_name)

    def cool(self: None, from_name: str) -> None:
        makerequest("bye", from_name)

    def cup(self: None, from_name: str) -> None:
        makerequest("bye", from_name)

    def dalton(self: None, name: str, from_name: str) -> None:
        makerequest("dalton", name, from_name)

    def deraadt(self: None, name: str, from_name: str) -> None:
        makerequest("deraadt", name, from_name)

    def diabetes(self: None, from_name: str) -> None:
        makerequest("diabetes", from_name)

    def donut(self: None, name: str, from_name: str) -> None:
        makerequest("donut", name, from_name)

    def dosomething(self: None, do: str, something: str,
                    from_name: str) -> None:
        makerequest("dosomething", name, something, from_name)

    def equity(self: None, name: str, from_name: str) -> None:
        makerequest("equity", name, from_name)

    def everyone(self: None, from_name: str) -> None:
        makerequest("everyone", from_name)

    def everything(self: None, from_name: str) -> None:
        makerequest("everthing", from_name)

    def family(self: None, from_name: str) -> None:
        makerequest("family", from_name)

    def fascinating(self: None, from_name: str) -> None:
        makerequest("fascinating", from_name)

    def field(self: None, name: str, from_name: str, reference: str) -> None:
        makerequest("field", name, from_name, reference)

    def flying(self: None, from_name: str) -> None:
        makerequest("flying", from_name)

    def fyyff(self: None, from_name: str) -> None:
        makerequest("fyyff", from_name)

    def gfy(self: None, name: str, from_name: str) -> None:
        makerequest("gfy", name, from_name)

    def give(self: None, from_name: str) -> None:
        makerequest("give", from_name)

    def greed(self: None, noun: str, from_name: str) -> None:
        makerequest("greed", noun, from_name)

    def horse(self: None, from_name: str) -> None:
        makerequest("horse", from_name)

    def immensity(self: None, from_name: str) -> None:
        makerequest("immensity", from_name)

    def ing(self: None, name: str, from_name: str) -> None:
        makerequest("ing", name, from_name)

    def life(self: None, from_name: str) -> None:
        makerequest("life", from_name)

    def keep(self: None, name: str, from_name: str) -> None:
        makerequest("keep", name, from_name)

    def keepcalm(self: None, reaction: str, from_name: str) -> None:
        makerequest("keepcalm", reaction, from_name)

    def king(self: None, name: str, from_name: str) -> None:
        makerequest("king", name, from_name)

    def linus(self: None, name: str, from_name: str) -> None:
        makerequest("linus", name, from_name)

    def look(self: None, name: str, from_name: str) -> None:
        makerequest("look", name, from_name)

    def looking(self: None, from_name: str) -> None:
        makerequest("looking", from_name)

    def madison(self: None, name: str, from_name: str) -> None:
        makerequest("madison", name, from_name)

    def maybe(self: None, from_name: str) -> None:
        makerequest("maybe", from_name)

    def me(self: None, from_name: str) -> None:
        makerequest("me", from_name)

    def mornin(self: None, from_name: str) -> None:
        makerequest("mornin", from_name)

    def no(self: None, from_name: str) -> None:
        makerequest("no", from_name)

    def nugget(self: None, name: str, from_name: str) -> None:
        makerequest("nugget", name, from_name)

    def off(self: None, name: str, from_name: str) -> None:
        makerequest("off", name, from_name)

    def offwith(self: None, behavior: str, from_name: str) -> None:
        makerequest("off-with", behavior, from_name)

    def outside(self: None, name: str, from_name: str) -> None:
        makerequest("outside", name, from_name)

    def particular(self: None, thing: str, from_name: str) -> None:
        makerequest("particular", thing, from_name)

    def pink(self: None, from_name: str) -> None:
        makerequest("pink", from_name)

    def problem(self: None, name: str, from_name: str) -> None:
        makerequest("problem", name, from_name)

    def programmer(self: None, from_name: str) -> None:
        makerequest("programmer", from_name)

    def pulp(self: None, name: str, from_name: str) -> None:
        makerequest("pulp", name, from_name)

    def question(self: None, from_name: str) -> None:
        makerequest("question", from_name)

    def retard(self: None, from_name: str) -> None:
        makerequest("retard", from_name)

    def ridiculous(self: None, from_name: str) -> None:
        makerequest("ridiculous", from_name)

    def rtfm(self: None, from_name: str) -> None:
        makerequest("rtfm", from_name)

    def sake(self: None, from_name: str) -> None:
        makerequest("sake", from_name)

    def shakespeare(self: None, name: str, from_name: str) -> None:
        makerequest("shakespeare", name, from_name)

    def shit(self: None, from_name: str) -> None:
        makerequest("shit", from_name)

    def shutup(self: None, name: str, from_name: str) -> None:
        makerequest("shutup", name, from_name)

    def single(self: None, from_name: str) -> None:
        makerequest("single", from_name)

    def thanks(self: None, from_name: str) -> None:
        makerequest("thanks", from_name)

    def that(self: None, from_name: str) -> None:
        makerequest("that", from_name)

    def think(self: None, name: str, from_name: str) -> None:
        makerequest("think", name, from_name)

    def thinking(self: None, name: str, from_name: str) -> None:
        makerequest("thinking", name, from_name)

    def this(self: None, from_name: str) -> None:
        makerequest("this", from_name)

    def thumbs(self: None, name: str, from_name: str) -> None:
        makerequest("thumbs", name, from_name)

    def too(self: None, from_name: str) -> None:
        makerequest("too", from_name)

    def tucker(self: None, from_name: str) -> None:
        makerequest("tucker", from_name)

    def what(self: None, from_name: str) -> None:
        makerequest("what", from_name)

    def xmas(self: None, name: str, from_name: str) -> None:
        makerequest("xmas", name, from_name)

    def yoda(self: None, name: str, from_name: str) -> None:
        makerequest("yoda", name, from_name)

    def you(self: None, name: str, from_name: str) -> None:
        makerequest("you", name, from_name)

    def zayn(self: None, from_name: str) -> None:
        makerequest("zayn", from_name)

    def zero(self: None, from_name: str) -> None:
        makerequest("zero", from_name)
