"""
Cross-docking truck data.

This data is generated by a generate_dataset.py script.

Created: Feb 18, 2019 at 07:29:59 PM

Copyright (c) 2022, Krerkkiat Chusap
This souce code is licensed under BSD 3-Clause "New" or "Revised" License (see LICENSE for details).
"""
from pathlib import Path

# Problem data.
name = Path(__file__).stem
inbound_gate_count = 1
outbound_gate_count = 1

# Parameters used to generate this data.
number_of_total_product_types = 9
product_per_truck_rate = 0.35
possible_inbound_total_product = [250, 340]

# Truck data.
_inbound_truck_raw_data = [
    [0, 0, 38, 68, 0, 0, 0, 31, 113],
    [74, 27, 0, 54, 0, 64, 115, 6, 0],
    [0, 85, 0, 38, 54, 0, 0, 73, 0],
]

_outbound_truck_raw_data = [
    [7, 1, 2, 13, 8, 18, 50, 3, 61],
    [6, 59, 2, 13, 0, 4, 6, 5, 9],
    [40, 11, 5, 59, 6, 28, 35, 35, 21],
    [6, 34, 12, 55, 2, 0, 9, 56, 6],
    [15, 7, 17, 20, 38, 14, 15, 11, 16],
]

# Derived data.
inbound_truck_count = len(_inbound_truck_raw_data)
outbound_truck_count = len(_outbound_truck_raw_data)
total_truck_count = inbound_truck_count + outbound_truck_count
