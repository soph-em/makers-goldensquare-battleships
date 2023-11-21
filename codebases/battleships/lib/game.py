from lib.ship import Ship
from lib.ship_placement import ShipPlacement


class Game:
    def __init__(self, rows=10, cols=10):
        self.ship_placement_list = []
        self.rows = rows
        self.cols = cols
        self.unplaced_ships_list = [
            Ship(2),
            Ship(3),
            Ship(3),
            Ship(4),
            Ship(5),
        ]
        self.placed_ships_list = []

    def unplaced_ships(self):
        return self.unplaced_ships_list

    def place_ship(self, length, orientation, row, col):
        if orientation == "vertical":
            if row < 0 or row > self.rows or (row + length) > self.rows:
                raise ValueError("Invalid placement: ship overlaps board edge")
        elif orientation == "horizontal":
            if col < 0 or col > self.cols or (col + length) > self.cols:
                raise ValueError("Invalid placement: ship overlaps board edge")
        ship_placement = ShipPlacement(
        length=length,
        orientation=orientation,
        row=row,
        col=col,
        )
        self.ship_placement_list.append(ship_placement)
        self.placed_ships_list.append(
            self.unplaced_ships_list.pop(
                [self.unplaced_ships_list.index(ship) for ship in self.unplaced_ships_list 
                if ship.length == length][0]
                )
            )
        print(self.placed_ships_list, "\n", self.unplaced_ships_list)
        

    def ship_at(self, row, col):
        for ship_placement in self.ship_placement_list:
            if ship_placement.covers(row, col):
                return True
        return False
