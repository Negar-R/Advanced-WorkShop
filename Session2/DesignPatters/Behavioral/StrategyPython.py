class Context:
    def __init__(self, **kwargs):
        for name, imple in kwargs.items():
            setattr(self, name, imple)

    def chagho(self):
        print("chagho!")

    def mosalsal(self):
        print("Mosalsal!")


def tank():
    print("tank!")


def mine():
    print("mine!")


def client():
    ashkan = Context(tank=tank)
    GhamarAli = Context(tank=tank, mine=mine)
    return ashkan, GhamarAli
    # ashkan.tank()
    # GhamarAli.mine()
    # ashkan.chagho()


if __name__ == "__main__":
    rTuple = client()
    rTuple[0].tank()