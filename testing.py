from classes import Tile
from classes import Side, SideType

start_tile = Tile()
start_tile.id = 0
start_tile.image = ""
start_tile.cloister = False
start_tile.sides[Side.North] = SideType.City
start_tile.sides[Side.East] = SideType.Road
start_tile.sides[Side.South] = SideType.Farm
start_tile.sides[Side.West] = SideType.Road
