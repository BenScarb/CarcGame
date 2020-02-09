from classes import Tile, Route
from classes import Side, SideType, EndPoints

import json

start_tile = Tile()
start_tile.id = 0
start_tile.image = ""
start_tile.cloister = False
start_tile.sides[Side.North] = SideType.City
start_tile.sides[Side.East] = SideType.Road
start_tile.sides[Side.South] = SideType.Farm
start_tile.sides[Side.West] = SideType.Road

newRoute = Route()
newRoute.rid = 10
newRoute.touchingF.append(1)
newRoute.touchingF.append(3)
newRoute.endpoints.append(EndPoints.TopLeft)
newRoute.endpoints.append(EndPoints.LeftTop)
newRoute.meeple_pos = (100, 100)

start_tile.routes.append(newRoute)

newRoute = Route()
newRoute.rid = 9
newRoute.touchingF.append(2)
newRoute.touchingF.append(1)
newRoute.endpoints.append(EndPoints.TopRight)
newRoute.endpoints.append(EndPoints.LeftTop)
newRoute.meeple_pos = (200, 200)

start_tile.routes.append(newRoute)

print("-Dictionary- \n")
print(dict(start_tile))
print("\n-JSON- \n")
print(json.dumps(dict(start_tile), sort_keys=True, indent=4))
