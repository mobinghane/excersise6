class KrustyKrab:
    def __init__(self, data):
        self.data = data

    def mr_krabs(self):
        for i in self.data:
            if i.startswith("m"):
                print(i.replace("tt", "o"))

class SpongeBob(KrustyKrab):
    def __init__(self, data):
        super().__init__(data)

    def bubble_buddy(self):
        self.data.sort(key=lambda x: int("".join(sorted(x))))
        print("".join(self.data))

class Squidward(KrustyKrab):
    def __init__(self, data):
        super().__init__(data)

    def clarinet(self):
        for i in self.data:
            if "xxx" in i:
                print("(0_0)", end="")
            else:
                print(i, end="")

data = input().split()
if data[0].startswith("m"):
    krusty_krab = KrustyKrab(data)
    krusty_krab.mr_krabs()
elif data[0].startswith("sb"):
    spongebob = SpongeBob(data)
    spongebob.bubble_buddy()
elif data[0].startswith("s") and data[0][1] != "b":
    squidward = Squidward(data)
    squidward.clarinet()
else:
    print("invalid input")
