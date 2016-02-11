from typing import Tuple, List, Optional
from util import distance_to

__author__ = 'erb'

drone_capacity = 0

product_weights = []
warehouses = []

class Positionable:
    def __init__(self, position: Tuple[int]):
        self._position = position

    @property
    def pos(self):
        return self._position

    @pos.setter
    def pos(self, pos):
        self._position = pos


class Turndependent:
    def __init__(self):
        self._at_turn = 0

    @property
    def turn(self) -> int:
        return self._at_turn


class House(Positionable):
    pass


class Warehouse(Positionable):
    def __init__(self, position: Tuple[int], stock: List[int]):
        Positionable.__init__(self, position)
        self._stock = stock

    @property
    def stock(self):
        return self._stock

    def has_in_stock(self, product_id) -> bool:
        return self._stock[product_id] > 0


def availability(product_id, destination):
    av = 0
    for warehouse in warehouses:
        # TODO: Bench **1 vs **2 on dist
        av += warehouse.stock[product_id] / distance_to(destination, warehouse.pos)
    return av


class Deliverable(Turndependent):
    def __init__(self, destination_pos, product_id, order_size):
        Turndependent.__init__(self)
        self._product_id = product_id
        self._destination_pos = destination_pos
        self._current_pos = None
        self._order_size = order_size

    @property
    def current_pos(self) -> Optional[Tuple[int]]:
        return self._current_pos

    @property
    def destination_pos(self) -> Tuple[int]:
        return self._destination_pos

    @property
    def current_pos(self) -> Optional[Tuple[int]]:
        return self._current_pos

    @current_pos.setter
    def current_pos(self, pos):
        self._current_pos = pos

    @property
    def weight(self) -> int:
        return product_weights[self._product_id]

    def priority(self):
        # TODO: Bench + vs *
        return 1/self._order_size * availability(self._product_id, self._destination_pos)


class Drone(Positionable, Turndependent):
    def __init__(self, position):
        Positionable.__init__(self, position)
        Turndependent.__init__(self)
        self._inventory = []

    @property
    @staticmethod
    def capacity():
        return drone_capacity

    @capacity.setter
    def capacity(self, new_capacity):
        global drone_capacity
        drone_capacity = new_capacity

    def load(self, deliverable: Deliverable, warehouse: Warehouse):
        self._at_turn += distance_to(self.pos, warehouse.pos)
        self.pos = warehouse.pos
        pass

    def deliver(self, pos):
        self._at_turn += distance_to(self.pos, pos)
        self.pos = pos
        pass

    def unload(self, warehouse: Warehouse):
        self._at_turn += distance_to(self.pos, warehouse.pos)
        # Special
        pass

    def wait(self, turns: int):
        # Special
        self._at_turn += turns

"""
class Order:
    def __init__(self, destination: House, items: List[int]):
        self._destination = destination
        self._items = items

    def undelivered_items(self) -> List[Deliverable]:
        return list()
"""

