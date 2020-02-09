from allowjson import Jsonable
from enum import Enum, auto

#Side = Enum("Side", "North East South West")
#SideType = Enum("SidType", "Farm Road City River")

class SideType(str, Enum):
    Farm = "farm"
    Road = "road"
    City = "city"
    River = "river"

    def __str__(self):
        return '{0}'.format(self.value)

class Side(str, Enum):
    North = "north"
    East = "east"
    South = "south"
    West = "west"

    def __str__(self):
        return '{0}'.format(self.value)


class EndPoints(int, Enum):
    TopLeft = 1
    TopMiddle = 2
    TopRight = 3
    LeftTop = 4
    LeftMiddle = 5
    LeftBottom = 6
    BottomRight = -3
    BottomMiddle = -2
    BottomLeft = -3
    RightBottom = -6
    RightMiddle = -5
    RightTop = -4
    Centre = 0

    def __str__(self):
        return '{0}'.format(self.value)
    

class Tile(Jsonable):
    def __init__(self):
        self.id = -1
        self.image = ""
        self.cloister = False
        self.sides = dict()
        self.routes = []

class Route(Jsonable):
    def __init__(self):
        self.rid = -1
        self.touchingF = []
        self.pendant = False
        self.endpoints = []
        self.meeple_pos = (0, 0)