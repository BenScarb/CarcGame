from classes import Tile, Route
from classes import Side, SideType, EndPoints

import json

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
newRoute.touching_cities.append("1-1")
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

dump = []
dump.append(dict(start_tile))
start_tile.id = 2
start_tile.order = 2
dump.append(dict(start_tile))

print("-Dictionary- \n")
print(dump)

json_dump = json.dumps(dump, sort_keys=False, indent=4)

print("---------------------------------------------------------")
more_tiles = Tile.Load_Tiles(json_dump)

test = []
for item in more_tiles:
    test.append(dict(item))
print(test)

