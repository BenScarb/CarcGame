from classes import Tile, Route
from classes import Side, SideType, EndPoints

import json
import jsonpickle

start_tile = Tile()
start_tile.id = 1
start_tile.order = 1
start_tile.image = "base64Image"
start_tile.cloister = False
start_tile.sides[Side.North] = SideType.City
start_tile.sides[Side.East] = SideType.Road
start_tile.sides[Side.South] = SideType.Farm
start_tile.sides[Side.West] = SideType.Road

newRoute = Route()
newRoute.rid = "1-1"
newRoute.route_type = SideType.City
newRoute.endpoints.append(EndPoints.TopLeft)
newRoute.endpoints.append(EndPoints.TopMiddle)
newRoute.endpoints.append(EndPoints.TopRight)
newRoute.meeple_pos = (100, 100)
start_tile.routes.append(newRoute)

newRoute = Route()
newRoute.rid = "1-2"
newRoute.route_type = SideType.Road
newRoute.endpoints.append(EndPoints.LeftMiddle)
newRoute.endpoints.append(EndPoints.RightMiddle)
newRoute.meeple_pos = (200, 200)
start_tile.routes.append(newRoute)

newRoute = Route()
newRoute.rid = "1-3"
newRoute.touchingF = "1-1"
newRoute.route_type = SideType.Farm
newRoute.endpoints.append(EndPoints.LeftTop)
newRoute.endpoints.append(EndPoints.RightTop)
start_tile.routes.append(newRoute)

newRoute = Route()
newRoute.rid = "1-4"
newRoute.route_type = SideType.Farm
newRoute.endpoints.append(EndPoints.LeftBottom)
newRoute.endpoints.append(EndPoints.BottomLeft)
newRoute.endpoints.append(EndPoints.BottomMiddle)
newRoute.endpoints.append(EndPoints.BottomRight)
newRoute.endpoints.append(EndPoints.RightBottom)
start_tile.routes.append(newRoute)

#dump = dict()
#dump[1] = start_tile
#start_tile.id = 2
#dump[2] = start_tile

dump = []
dump.append(dict(start_tile))
start_tile.id = 2
dump.append(dict(start_tile))


def Load_Tiles(json_file):
    new_tiles = []
    json_tiles = json.loads(json_file)
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
            new_route.endpoints = []
            for jsonRoutePart in jsonRoute["endpoints"]:
                new_route.endpoints.append(EndPoints(jsonRoutePart))
            
            ntile.routes.append(new_route)

        new_tiles.append(ntile)
    
    return new_tiles


print("-Dictionary- \n")
print(dump)
#print("\n-JSON- \n")
json_dump = json.dumps(dump, sort_keys=True, indent=4)
#print(json_dump)
json_obj = json.loads(json_dump)
#print(json_obj[0]["id"])
#print(json_obj[1]["id"])
print("---------------------------------------------------------")
more_tiles = Load_Tiles(json_dump)
#print(more_tiles)
test = []
for item in more_tiles:
    test.append(dict(item))
print(test)

