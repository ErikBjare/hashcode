
from typing import List, Tuple

import classes
from classes import Drone, Warehouse, Deliverable
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
    classes.product_weights = input_ints()

    """Warehouses"""
    number_of_warehouses = input_int()
    for _ in range(number_of_warehouses):
        position = input_intpair()
        product_stock = input_ints()
        classes.warehouses.append(Warehouse(position, product_stock))


    """Drones"""
    drones = [Drone(classes.warehouses[0].pos) for _ in range(n_drones)]
    Drone.capacity = max_load

    """Customer orders"""
    number_of_orders = input_int()
    for order_id, _ in enumerate(range(number_of_orders)):
        position = input_intpair()
        number_of_products_ordered = input_int()
        products_ordered = input_ints()
        classes.deliverables.extend([Deliverable(position, product_id, order_id, classes.product_weights[product_id]) for product_id in products_ordered])

    try:
        input()
    except EOFError:
        pass
    else:
        print("There was something left in the input data, exiting")
        exit(1)

    #print("Warehouses: {}, Drones: {}, Deliverables: {}".format(len(classes.warehouses), n_drones, len(deliverables)))
    #print("Drone capacity: {}".format(Drone.capacity))

    def get_drones_by_turns():
        return sorted(drones, key=lambda d: d.turn)

    def get_first_available_drone():
        return get_drones_by_turns()[0]

    def get_optimal_drone(destination):
        cost = [drone.turn + distance_to(drone.pos, destination) for drone in drones]
        i = cost.index(min(cost))
        return drones[i]

    def get_closest_deliverable(pos):
        return sorted(classes.deliverables, key=lambda o: distance_to(o.destination_pos, pos))

    def get_warehouses_sorted_by_distance(pos):
        return sorted(classes.warehouses, key=lambda o: distance_to(o.pos, pos))

    def get_closest_warehouse_with_product(pos, product_id):
        for warehouse in get_warehouses_sorted_by_distance(pos):
            if warehouse.has_in_stock(product_id):
                return warehouse

    sdel = sorted(classes.deliverables, key=lambda d: d.priority())
    while True:
        if len(sdel) < 1:
            break
        deliverable = sdel.pop(0)
        # TODO: Get closest available drone
        warehouse = get_closest_warehouse_with_product(deliverable.destination_pos, deliverable._product_id)
        drone = get_optimal_drone(warehouse.pos)
        loaded = drone.load(deliverable, warehouse)
        for _ in range(loaded-1):
            sdel.pop(0)
        drone.deliver(deliverable)
        #print("Delivered")

    print(get_drones_by_turns()[-1].turn, deadline)
    #print("Done, all delivered")

    """
    min_turn = 0
    while len(deliverables) > 0 or deadline < min_turn:
        drone = get_first_available_drone()
        deliverable = get_closest_deliverable(drone.pos)
        warehouse_with_deliverable = get_closest_warehouse_with_product(deliverable.)
        get_first_available_drone().load(deliverable)
    """

if __name__ == "__main__":
    main()
