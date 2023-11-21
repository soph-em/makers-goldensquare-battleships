from dataclasses import dataclass

@dataclass
class Ship:
    length: int

    # def __init__(self): #untested
    #     self.placed = False
    #     self.sunk = False
    #     self.hit = [False] * self.length

    # def is_sunk(self): #untested
    #     if all(self.hit):
    #         self.sunk = True
    #     return self.sunk