class Robot :
    def __init__(self,name,color,weight):
        self.name=name
        self.color=color
        self.weight=weight
    def introduce_self(self):
        print("my name is "+ self.name)

r1=Robot("tom","red",30)
r2=Robot("jerry","blue",90)
