class Athlete:
    def __init__(self,value=0):
        self.thing = value
    def how_big(self):
        return(len(self.thing))

d = Athlete("Holy Grail")
print(d.how_big())