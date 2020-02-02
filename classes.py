from enum import Enum

Side = Enum("Side", "North East South West")
SideType = Enum("SidType", "Farm Road City River")


class Tile(object):
    def __init__(self):
        self.id = -1
        self.image = ""
        self.cloister = False
        self.sides = dict()
        self.routes = []

class Route(object):
    def __init__(self):
        self.rid = -1
        self.touchingF = []
        self.pendant = False
        self.endpoints = []
        self.meeple_pos = (0, 0)
    

