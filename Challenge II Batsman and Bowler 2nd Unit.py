class Batsman:
    def __init__(self, name):
        self.name = name

    def play(self):
        print(f"{self.name} is batting.")
class Bowler:
    def __init__(self, name):
        self.name = name

    def play(self):
        print(f"{self.name} is bowling.")
batsman1 = Batsman("Sachin")
bowler1 = Bowler("Warne")
batsman1.play()
bowler1.play()