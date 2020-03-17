from allowjson import Jsonable
from enum import Enum, auto
import json

class SideType(str, Enum):
    Invalid = "invalid"
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
        self.order = -1
        self.image = ""
        self.cloister = False
        self.sides = dict()
        self.routes = []
     
    @staticmethod
    def Load_Tiles(jsonText):
        new_tiles = []
        json_tiles = json.loads(jsonText)
        for tile in json_tiles:
            ntile = Tile()
            ntile.id = tile["id"]
            ntile.order = tile["order"]
            ntile.image = tile["image"]
            ntile.cloister = tile["cloister"]
            for jsonSide in tile["sides"]:
                ntile.sides[Side(jsonSide)] = SideType(tile["sides"][jsonSide])

            
            for jsonRoute in tile["routes"]:
                new_route = Route()
                new_route.rid = jsonRoute["rid"]
                new_route.route_type = SideType(jsonRoute["route_type"])
        
                new_route.meeple_pos = (jsonRoute["meeple_pos"][0], jsonRoute["meeple_pos"][1])

                for json_touching in jsonRoute["touching_cities"]:
                    new_route.touching_cities.append(json_touching)

                for jsonRoutePart in jsonRoute["endpoints"]:
                    new_route.endpoints.append(EndPoints(jsonRoutePart))
                
                ntile.routes.append(new_route)

            new_tiles.append(ntile)
        
        return new_tiles


class Route(Jsonable):
    def __init__(self):
        self.rid = -1
        self.route_type = SideType.Invalid
        self.touching_cities = []
        self.pendant = False
        self.endpoints = []
        self.meeple_pos = (0, 0)