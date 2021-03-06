"""
Cross-docking truck data.

This data is generated by a generate_dataset.py script.

Created: Feb 18, 2019 at 07:30:03 PM

Copyright (c) 2022, Krerkkiat Chusap
This souce code is licensed under BSD 3-Clause "New" or "Revised" License (see LICENSE for details).
"""
from pathlib import Path

# Problem data.
name = Path(__file__).stem
inbound_gate_count = 20
outbound_gate_count = 20

# Parameters used to generate this data.
number_of_total_product_types = 15
product_per_truck_rate = 0.35
possible_inbound_total_product = [250, 340]

# Truck data.
_inbound_truck_raw_data = [
    [98, 0, 0, 48, 0, 0, 0, 0, 78, 0, 0, 0, 0, 26, 0],
    [0, 0, 0, 0, 0, 9, 36, 9, 0, 0, 0, 0, 0, 0, 196],
    [0, 0, 0, 9, 21, 116, 0, 0, 0, 104, 0, 0, 0, 0, 0],
    [49, 16, 0, 0, 169, 0, 0, 0, 0, 0, 16, 0, 0, 0, 0],
    [77, 0, 0, 0, 0, 0, 0, 0, 0, 67, 67, 0, 0, 0, 39],
    [143, 0, 0, 0, 0, 0, 0, 19, 0, 76, 0, 12, 0, 0, 0],
    [0, 0, 0, 0, 23, 0, 0, 0, 115, 0, 0, 0, 73, 39, 0],
    [105, 99, 0, 0, 0, 0, 0, 0, 0, 27, 12, 61, 36, 0, 0],
    [0, 13, 117, 54, 0, 0, 112, 0, 0, 0, 9, 35, 0, 0, 0],
    [0, 0, 69, 0, 104, 0, 0, 12, 59, 0, 0, 88, 8, 0, 0],
    [0, 0, 71, 3, 106, 0, 70, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 14, 0, 5, 0, 7, 0, 0, 168, 62, 0, 0, 0, 84, 0],
    [4, 0, 0, 69, 37, 0, 140, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 109, 0, 0, 0, 0, 0, 0, 31, 110, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 30, 0, 0, 0, 0, 27, 0, 0, 186, 0, 0],
    [81, 0, 0, 0, 0, 25, 63, 0, 0, 0, 0, 81, 0, 0, 0],
    [0, 36, 0, 0, 0, 69, 0, 27, 37, 0, 0, 66, 0, 0, 105],
    [0, 0, 0, 36, 0, 52, 0, 0, 0, 0, 3, 0, 0, 0, 159],
    [67, 0, 0, 45, 0, 0, 96, 64, 0, 0, 0, 0, 0, 34, 34],
    [0, 0, 2, 0, 0, 0, 0, 0, 0, 38, 0, 0, 40, 170, 0],
    [0, 8, 0, 0, 0, 97, 84, 0, 0, 0, 0, 0, 61, 0, 0],
    [0, 112, 0, 0, 0, 0, 0, 21, 0, 0, 91, 26, 0, 0, 0],
    [34, 28, 0, 65, 0, 74, 0, 0, 0, 0, 0, 0, 0, 119, 20],
    [0, 0, 14, 0, 48, 86, 0, 0, 0, 0, 51, 0, 81, 0, 60],
    [0, 26, 0, 0, 0, 23, 0, 188, 0, 0, 0, 0, 0, 0, 13],
    [27, 0, 6, 17, 0, 33, 0, 0, 0, 0, 0, 69, 0, 188, 0],
    [0, 0, 0, 0, 121, 0, 0, 0, 55, 0, 4, 59, 0, 11, 90],
    [135, 0, 0, 0, 25, 0, 0, 48, 0, 0, 0, 0, 0, 0, 42],
    [0, 47, 0, 0, 18, 0, 23, 0, 130, 0, 0, 84, 0, 0, 38],
    [0, 0, 0, 0, 0, 0, 111, 0, 41, 0, 0, 0, 15, 83, 0],
    [0, 8, 0, 0, 0, 0, 0, 0, 37, 0, 193, 0, 0, 12, 0],
    [0, 3, 0, 3, 0, 0, 240, 4, 0, 0, 0, 0, 0, 0, 0],
    [0, 59, 0, 0, 2, 0, 0, 7, 0, 0, 0, 40, 205, 27, 0],
    [0, 6, 0, 46, 0, 0, 0, 178, 0, 0, 20, 0, 0, 0, 0],
    [0, 122, 24, 0, 0, 0, 0, 0, 0, 10, 40, 120, 0, 0, 24],
    [0, 0, 20, 0, 17, 20, 0, 0, 0, 24, 0, 0, 54, 0, 205],
    [34, 48, 0, 0, 0, 0, 12, 0, 0, 0, 0, 96, 47, 0, 103],
    [0, 79, 0, 0, 86, 52, 0, 0, 33, 0, 0, 0, 0, 0, 0],
    [131, 67, 0, 0, 0, 15, 0, 0, 6, 0, 88, 0, 33, 0, 0],
    [4, 0, 0, 6, 0, 21, 109, 0, 63, 0, 137, 0, 0, 0, 0],
    [48, 0, 0, 0, 0, 0, 0, 0, 8, 0, 25, 0, 169, 0, 0],
    [0, 9, 0, 0, 120, 0, 0, 116, 0, 0, 0, 0, 5, 0, 0],
    [18, 0, 0, 113, 0, 0, 77, 0, 0, 0, 42, 0, 0, 0, 0],
    [0, 0, 0, 0, 75, 0, 95, 74, 0, 0, 0, 0, 6, 0, 0],
    [0, 0, 138, 28, 21, 0, 0, 0, 0, 0, 0, 0, 63, 0, 0],
    [0, 0, 0, 23, 21, 0, 6, 0, 0, 0, 0, 0, 1, 160, 129],
    [0, 24, 0, 0, 0, 0, 1, 0, 0, 0, 0, 146, 0, 0, 79],
    [13, 0, 0, 0, 14, 0, 0, 122, 101, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 78, 95, 0, 0, 59, 0, 0, 18, 0, 0],
    [0, 0, 0, 0, 171, 65, 0, 0, 0, 0, 0, 8, 0, 0, 6],
    [0, 0, 0, 78, 0, 13, 30, 0, 66, 0, 0, 0, 0, 89, 64],
    [0, 44, 0, 0, 0, 0, 0, 144, 33, 0, 0, 29, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 145, 0, 0, 0, 46, 59, 0, 0],
    [0, 0, 0, 41, 56, 0, 25, 80, 0, 134, 0, 0, 0, 4, 0],
    [54, 118, 0, 13, 76, 0, 75, 4, 0, 0, 0, 0, 0, 0, 0],
    [22, 0, 190, 16, 0, 0, 0, 0, 0, 22, 0, 0, 0, 0, 0],
    [0, 0, 136, 0, 109, 0, 0, 20, 0, 0, 0, 55, 15, 5, 0],
    [0, 0, 0, 62, 0, 74, 29, 0, 125, 0, 0, 0, 0, 23, 27],
    [0, 0, 0, 11, 0, 0, 113, 0, 0, 0, 0, 0, 12, 114, 0],
    [83, 0, 0, 0, 0, 0, 54, 33, 0, 80, 0, 0, 0, 0, 0],
]

_outbound_truck_raw_data = [
    [3, 9, 2, 2, 2, 19, 15, 13, 0, 29, 1, 7, 13, 20, 35],
    [45, 10, 8, 22, 5, 7, 33, 2, 63, 2, 8, 1, 4, 2, 6],
    [1, 5, 5, 2, 4, 1, 27, 29, 3, 0, 6, 5, 8, 16, 1],
    [3, 25, 3, 5, 6, 0, 17, 41, 4, 4, 2, 22, 4, 8, 14],
    [10, 21, 1, 0, 7, 19, 51, 6, 4, 5, 6, 6, 7, 1, 9],
    [7, 6, 16, 0, 24, 4, 3, 3, 1, 2, 26, 20, 8, 4, 4],
    [10, 4, 10, 19, 23, 4, 7, 12, 3, 8, 7, 1, 7, 19, 31],
    [15, 25, 6, 12, 5, 1, 17, 5, 68, 12, 1, 0, 6, 2, 2],
    [34, 2, 50, 6, 5, 15, 8, 0, 13, 5, 7, 1, 12, 29, 24],
    [5, 17, 11, 0, 6, 6, 1, 3, 11, 3, 6, 2, 12, 7, 10],
    [44, 10, 13, 3, 10, 7, 1, 19, 22, 1, 0, 18, 1, 14, 0],
    [7, 15, 0, 19, 21, 1, 10, 9, 6, 9, 36, 49, 10, 9, 0],
    [19, 11, 3, 0, 3, 2, 34, 22, 17, 4, 1, 20, 9, 5, 5],
    [3, 29, 22, 2, 11, 3, 8, 3, 7, 16, 4, 2, 1, 7, 1],
    [11, 6, 2, 4, 16, 25, 25, 5, 3, 1, 1, 16, 4, 0, 1],
    [22, 9, 7, 16, 8, 7, 9, 28, 38, 4, 4, 7, 30, 23, 2],
    [2, 6, 5, 5, 4, 11, 30, 11, 5, 2, 3, 0, 1, 2, 14],
    [15, 3, 10, 16, 2, 10, 52, 4, 7, 7, 6, 15, 7, 3, 42],
    [1, 14, 22, 1, 16, 25, 19, 10, 3, 22, 13, 8, 18, 4, 7],
    [6, 12, 17, 1, 2, 6, 20, 7, 1, 0, 3, 22, 15, 45, 35],
    [5, 22, 15, 9, 13, 3, 7, 3, 42, 4, 4, 2, 4, 8, 16],
    [4, 21, 11, 19, 23, 2, 15, 7, 45, 10, 2, 4, 18, 43, 8],
    [6, 1, 2, 0, 16, 4, 21, 11, 5, 3, 3, 35, 15, 26, 3],
    [11, 18, 5, 12, 24, 0, 25, 31, 14, 5, 3, 12, 8, 2, 67],
    [24, 0, 0, 5, 10, 1, 12, 4, 1, 11, 3, 8, 2, 10, 4],
    [0, 30, 2, 18, 9, 2, 3, 64, 14, 2, 4, 15, 14, 13, 5],
    [25, 29, 14, 19, 24, 7, 31, 2, 31, 4, 10, 8, 2, 8, 6],
    [46, 60, 2, 4, 0, 8, 19, 47, 1, 5, 11, 8, 2, 0, 0],
    [5, 1, 10, 3, 20, 5, 0, 1, 23, 26, 4, 0, 7, 1, 18],
    [4, 11, 10, 20, 1, 16, 4, 0, 12, 4, 6, 31, 2, 8, 12],
    [11, 12, 2, 29, 8, 5, 33, 6, 10, 4, 8, 0, 27, 3, 8],
    [32, 1, 1, 11, 23, 16, 14, 10, 6, 14, 3, 35, 31, 24, 16],
    [20, 15, 22, 5, 8, 17, 33, 2, 4, 9, 9, 34, 15, 5, 4],
    [6, 14, 0, 4, 17, 12, 12, 2, 5, 0, 3, 19, 5, 10, 10],
    [5, 7, 6, 0, 52, 16, 9, 10, 17, 1, 3, 7, 10, 5, 2],
    [2, 1, 5, 2, 16, 7, 8, 50, 36, 3, 1, 2, 12, 5, 0],
    [15, 7, 1, 24, 6, 9, 10, 5, 10, 3, 33, 6, 51, 8, 65],
    [9, 6, 5, 0, 6, 11, 16, 55, 2, 7, 12, 4, 14, 49, 37],
    [14, 4, 29, 0, 31, 10, 18, 35, 22, 2, 16, 11, 9, 0, 1],
    [19, 5, 7, 20, 5, 3, 46, 1, 5, 0, 9, 10, 9, 11, 18],
    [4, 18, 8, 12, 10, 8, 17, 6, 4, 3, 2, 37, 4, 5, 2],
    [1, 2, 16, 2, 8, 11, 12, 11, 18, 3, 13, 4, 12, 1, 18],
    [0, 9, 6, 7, 3, 5, 2, 24, 1, 11, 8, 14, 22, 28, 5],
    [2, 9, 7, 2, 10, 5, 2, 10, 1, 1, 5, 5, 49, 11, 36],
    [26, 16, 9, 19, 13, 2, 14, 53, 12, 4, 3, 10, 2, 1, 24],
    [10, 9, 6, 15, 5, 37, 15, 12, 6, 6, 13, 4, 18, 13, 3],
    [4, 2, 3, 26, 74, 2, 15, 18, 0, 25, 19, 2, 8, 3, 27],
    [4, 23, 5, 8, 5, 12, 3, 2, 1, 13, 2, 10, 18, 7, 3],
    [14, 13, 6, 16, 6, 30, 24, 5, 1, 4, 2, 2, 9, 7, 4],
    [3, 11, 7, 3, 1, 4, 33, 17, 1, 12, 11, 12, 7, 2, 9],
    [23, 14, 13, 7, 10, 10, 0, 18, 5, 8, 1, 0, 11, 3, 5],
    [8, 3, 31, 14, 14, 0, 3, 7, 1, 17, 1, 6, 10, 14, 9],
    [10, 7, 4, 4, 73, 3, 53, 7, 2, 13, 33, 11, 3, 13, 1],
    [1, 9, 1, 10, 29, 7, 11, 14, 7, 2, 10, 1, 3, 2, 4],
    [10, 12, 5, 21, 30, 9, 23, 12, 1, 12, 1, 19, 15, 23, 1],
    [0, 11, 5, 5, 0, 1, 7, 6, 33, 15, 9, 17, 10, 9, 25],
    [28, 3, 7, 5, 9, 5, 13, 14, 25, 5, 36, 1, 5, 11, 2],
    [6, 5, 5, 6, 23, 5, 10, 10, 3, 2, 4, 27, 36, 42, 2],
    [15, 15, 1, 1, 3, 4, 17, 3, 7, 8, 5, 6, 10, 37, 2],
    [6, 14, 1, 6, 8, 28, 12, 30, 9, 2, 1, 9, 2, 10, 9],
    [3, 2, 12, 25, 5, 3, 30, 17, 7, 4, 5, 42, 3, 33, 10],
    [16, 2, 9, 4, 21, 24, 9, 5, 18, 4, 10, 6, 9, 7, 11],
    [13, 1, 5, 2, 14, 2, 5, 4, 4, 10, 17, 6, 3, 10, 13],
    [16, 7, 5, 2, 38, 13, 15, 15, 9, 11, 10, 17, 1, 8, 16],
    [44, 2, 3, 5, 16, 11, 47, 22, 1, 6, 3, 3, 4, 8, 14],
    [10, 4, 13, 27, 25, 13, 20, 7, 9, 15, 3, 1, 2, 2, 5],
    [9, 34, 8, 0, 43, 3, 11, 10, 6, 8, 6, 7, 2, 4, 17],
    [9, 12, 5, 13, 1, 5, 34, 10, 20, 29, 13, 7, 3, 2, 35],
    [20, 16, 11, 4, 10, 22, 6, 16, 4, 1, 13, 10, 3, 46, 67],
    [5, 14, 2, 6, 16, 30, 25, 0, 22, 15, 16, 7, 21, 2, 0],
    [18, 14, 2, 12, 3, 24, 11, 8, 18, 8, 1, 5, 3, 17, 14],
    [23, 4, 4, 4, 10, 4, 26, 4, 4, 7, 12, 2, 5, 11, 36],
    [52, 39, 15, 11, 5, 3, 13, 17, 5, 14, 1, 11, 18, 3, 5],
    [27, 4, 7, 5, 6, 13, 6, 11, 4, 5, 15, 1, 12, 14, 38],
    [21, 4, 6, 1, 11, 2, 11, 20, 1, 18, 8, 9, 36, 10, 17],
    [17, 14, 3, 7, 3, 0, 50, 4, 3, 19, 13, 7, 19, 3, 1],
    [1, 3, 19, 5, 4, 9, 43, 15, 19, 9, 6, 26, 13, 31, 10],
    [3, 8, 6, 3, 25, 14, 18, 13, 21, 1, 1, 22, 42, 7, 4],
    [33, 10, 3, 12, 25, 0, 9, 9, 5, 0, 1, 28, 12, 26, 10],
    [8, 12, 1, 5, 17, 1, 29, 24, 0, 23, 0, 3, 5, 12, 24],
    [2, 11, 1, 1, 25, 11, 16, 15, 24, 12, 4, 2, 28, 16, 25],
    [0, 2, 2, 2, 22, 4, 1, 32, 19, 9, 6, 22, 29, 37, 68],
    [7, 16, 6, 6, 9, 1, 18, 2, 13, 3, 6, 0, 18, 26, 10],
    [6, 2, 5, 17, 6, 7, 45, 13, 10, 11, 3, 10, 0, 8, 31],
    [14, 2, 2, 1, 0, 2, 19, 1, 11, 18, 11, 4, 14, 25, 9],
    [13, 8, 6, 6, 7, 42, 10, 2, 4, 5, 5, 5, 6, 19, 17],
    [4, 3, 35, 1, 12, 2, 1, 0, 3, 41, 0, 14, 6, 1, 32],
    [16, 14, 10, 4, 8, 1, 3, 8, 6, 3, 27, 0, 22, 19, 20],
    [24, 2, 5, 3, 4, 2, 21, 17, 4, 19, 2, 7, 26, 4, 7],
    [15, 9, 2, 1, 14, 13, 12, 3, 17, 10, 1, 21, 6, 1, 11],
    [6, 2, 4, 3, 2, 20, 10, 26, 41, 26, 13, 7, 20, 16, 20],
    [8, 5, 8, 11, 31, 6, 19, 18, 6, 4, 6, 42, 7, 1, 10],
    [2, 16, 5, 3, 44, 6, 5, 18, 3, 0, 1, 8, 48, 9, 12],
    [16, 21, 2, 20, 2, 0, 13, 20, 48, 4, 21, 15, 4, 6, 16],
    [11, 3, 4, 7, 18, 2, 10, 2, 6, 3, 10, 22, 5, 0, 8],
    [9, 20, 17, 9, 57, 4, 8, 2, 10, 2, 5, 12, 4, 2, 1],
    [12, 5, 10, 6, 16, 19, 1, 11, 6, 21, 26, 10, 26, 5, 15],
    [7, 5, 11, 4, 21, 11, 45, 33, 16, 14, 1, 9, 11, 1, 6],
    [4, 2, 3, 9, 4, 57, 7, 0, 20, 0, 8, 14, 2, 12, 23],
    [2, 32, 2, 3, 44, 8, 5, 4, 17, 9, 21, 7, 1, 23, 11],
]

# Derived data.
inbound_truck_count = len(_inbound_truck_raw_data)
outbound_truck_count = len(_outbound_truck_raw_data)
total_truck_count = inbound_truck_count + outbound_truck_count
