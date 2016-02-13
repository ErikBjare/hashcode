
from typing import List, Tuple

from classes import Drone, Warehouse, Order
from util import distance_to

__author__ = 'erb'


def input_int() -> int:
    return int(input())


def input_ints() -> List[int]:
    return list(map(int, input().split()))


def input_intpair() -> Tuple[int]:
    return tuple(input_ints())


def main():
    rows, cols, n_drones, deadline, max_load = input_ints()

    """Products"""
    number_of_product_types = input_int()
    product_weights = input_ints()

    """Warehouses"""
    number_of_warehouses = input_int()
    warehouses = []
    for _ in range(number_of_warehouses):
        position = input_intpair()
        product_stock = input_ints()
        warehouses.append(Warehouse(position, product_stock))

    """Drones"""
    drones = [Drone(warehouses[0].pos) for _ in range(n_drones)]
    Drone.capacity = max_load

    """Customer orders"""
    number_of_orders = input_int()
    orders = []
    for _ in range(number_of_orders):
        position = input_intpair()
        number_of_products_ordered = input_int()
        products_ordered = input_ints()
        orders.append(Order(position, products_ordered))

    try:
        print(input())
    except EOFError:
        pass
    else:
        print("There was something left in the input data, exiting")
        exit(1)

    print("Warehouses: {}, Drones: {}, Orders: {}".format(len(warehouses), n_drones, len(orders)))
    print("Drone capacity: {}".format(Drone.capacity))

    def get_first_available_drone():
        return sorted(drones, key=lambda d: d.turn)[0]

    def get_closest_order(pos):
        return sorted(orders, key=lambda o: distance_to(o.pos, pos))

    print("First available drone: {}".format(get_first_available_drone()))

    min_turn = 0
    while len(orders) > 0 or deadline < min_turn:
        get_first_available_drone().load()

if __name__ == "__main__":
    main()
