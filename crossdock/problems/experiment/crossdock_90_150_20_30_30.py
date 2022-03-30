"""
Cross-docking truck data.

This data is generated by a generate_dataset.py script.

Created: Feb 18, 2019 at 07:30:04 PM

Copyright (c) 2022, Krerkkiat Chusap
This souce code is licensed under BSD 3-Clause "New" or "Revised" License (see LICENSE for details).
"""
from pathlib import Path

# Problem data.
name = Path(__file__).stem
inbound_gate_count = 30
outbound_gate_count = 30

# Parameters used to generate this data.
number_of_total_product_types = 20
product_per_truck_rate = 0.35
possible_inbound_total_product = [250, 340]

# Truck data.
_inbound_truck_raw_data = [
    [30, 0, 0, 14, 0, 0, 0, 16, 0, 0, 70, 0, 0, 0, 111, 0, 0, 0, 0, 99],
    [0, 37, 0, 0, 17, 0, 0, 0, 0, 35, 0, 215, 36, 0, 0, 0, 0, 0, 0, 0],
    [51, 0, 0, 0, 15, 0, 0, 0, 31, 0, 0, 0, 0, 0, 0, 0, 153, 0, 0, 0],
    [0, 26, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 75, 6, 0, 0, 143, 0],
    [88, 0, 0, 0, 0, 0, 0, 24, 0, 0, 0, 0, 0, 0, 117, 0, 21, 0, 0, 0],
    [0, 0, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 67, 0, 0, 0, 2, 0, 0, 166],
    [0, 0, 0, 80, 0, 0, 108, 0, 0, 0, 0, 35, 0, 0, 0, 0, 0, 27, 0, 0],
    [0, 0, 45, 0, 60, 0, 0, 35, 0, 0, 0, 0, 0, 0, 0, 110, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 24, 0, 0, 0, 56, 0, 119, 0, 0, 0, 0, 51],
    [153, 5, 0, 0, 0, 82, 0, 0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 139, 5, 0, 0, 71, 0, 0, 0, 0, 0, 40, 10, 75, 0, 0],
    [25, 0, 76, 0, 0, 0, 70, 0, 7, 0, 0, 0, 0, 0, 0, 0, 156, 0, 6, 0],
    [16, 0, 0, 0, 0, 0, 33, 0, 0, 0, 0, 0, 0, 0, 34, 0, 0, 167, 0, 0],
    [88, 0, 70, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 40, 52, 0, 0],
    [0, 0, 0, 22, 0, 0, 176, 0, 0, 0, 0, 16, 0, 0, 0, 10, 0, 0, 111, 5],
    [0, 0, 66, 45, 0, 0, 107, 0, 0, 0, 0, 0, 0, 0, 0, 32, 0, 0, 0, 0],
    [124, 0, 0, 0, 0, 0, 0, 0, 108, 0, 0, 0, 0, 0, 0, 0, 2, 16, 0, 0],
    [25, 127, 0, 0, 0, 0, 0, 21, 54, 0, 0, 0, 0, 0, 15, 98, 0, 0, 0, 0],
    [0, 0, 55, 0, 0, 0, 0, 0, 0, 30, 0, 0, 5, 29, 0, 0, 0, 94, 127, 0],
    [0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 75, 0, 91, 0, 0, 0, 61, 16, 87],
    [0, 0, 11, 0, 0, 0, 0, 70, 0, 0, 0, 0, 0, 0, 0, 0, 0, 67, 0, 102],
    [42, 0, 0, 0, 0, 0, 81, 42, 20, 0, 0, 0, 0, 0, 30, 0, 0, 125, 0, 0],
    [20, 0, 150, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 80, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 96, 2, 0, 0, 0, 0, 57, 97, 0, 50, 0, 38],
    [0, 0, 0, 26, 0, 0, 0, 15, 0, 0, 8, 0, 0, 256, 0, 0, 0, 0, 3, 32],
    [0, 0, 0, 0, 92, 0, 0, 0, 0, 0, 0, 70, 36, 33, 104, 0, 0, 0, 0, 5],
    [0, 0, 87, 0, 0, 0, 0, 17, 0, 0, 0, 0, 13, 0, 0, 133, 0, 0, 0, 0],
    [0, 10, 0, 0, 70, 0, 0, 0, 0, 0, 35, 0, 34, 0, 0, 0, 0, 8, 0, 183],
    [0, 30, 0, 0, 0, 52, 0, 157, 0, 0, 52, 46, 0, 0, 0, 0, 3, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 61, 0, 0, 0, 0, 59, 94, 36, 0, 0, 0],
    [0, 0, 0, 0, 53, 0, 0, 0, 0, 0, 41, 0, 0, 0, 0, 0, 0, 124, 0, 32],
    [0, 102, 0, 0, 0, 104, 22, 0, 0, 0, 0, 0, 0, 0, 0, 0, 22, 0, 0, 0],
    [21, 0, 0, 63, 0, 0, 0, 97, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 129, 27],
    [0, 0, 147, 9, 0, 26, 0, 0, 0, 0, 0, 17, 0, 0, 0, 0, 0, 98, 0, 43],
    [0, 0, 49, 0, 148, 0, 0, 88, 0, 0, 0, 14, 0, 0, 0, 0, 33, 0, 8, 0],
    [54, 0, 0, 0, 0, 0, 0, 91, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 87, 18],
    [0, 0, 0, 0, 0, 13, 0, 0, 0, 148, 80, 0, 0, 0, 9, 0, 0, 0, 0, 0],
    [0, 62, 0, 0, 0, 0, 0, 0, 0, 0, 81, 0, 0, 0, 0, 0, 0, 0, 25, 82],
    [27, 0, 0, 0, 32, 0, 0, 165, 0, 0, 41, 0, 0, 73, 0, 0, 0, 0, 2, 0],
    [0, 0, 5, 0, 127, 0, 0, 0, 0, 0, 0, 66, 22, 0, 0, 0, 0, 57, 63, 0],
    [0, 38, 23, 0, 124, 0, 0, 0, 0, 0, 0, 0, 57, 65, 33, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 30, 0, 0, 83, 0, 0, 0, 0, 0, 0, 0, 0, 61, 76, 0],
    [0, 0, 0, 87, 0, 0, 0, 3, 0, 0, 116, 0, 0, 0, 0, 0, 0, 0, 44, 0],
    [0, 0, 104, 0, 0, 20, 0, 0, 0, 0, 116, 0, 55, 11, 0, 0, 0, 0, 0, 34],
    [0, 0, 0, 0, 62, 0, 0, 0, 3, 0, 124, 44, 101, 0, 0, 0, 0, 6, 0, 0],
    [0, 0, 0, 77, 77, 130, 0, 11, 0, 0, 0, 33, 0, 0, 0, 0, 0, 0, 12, 0],
    [0, 0, 14, 0, 0, 5, 0, 0, 57, 0, 233, 0, 19, 0, 12, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 6, 0, 0, 0, 0, 126, 5, 0, 0, 113, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 52, 0, 0, 0, 0, 82, 0, 20, 0, 135, 0, 15, 36, 0, 0],
    [72, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20, 0, 0, 78, 0, 80, 0, 0, 0, 0],
    [15, 65, 0, 0, 0, 0, 0, 0, 0, 0, 169, 52, 0, 34, 0, 0, 0, 0, 0, 5],
    [103, 81, 0, 0, 0, 0, 0, 0, 0, 122, 23, 0, 0, 0, 0, 0, 7, 0, 0, 4],
    [0, 0, 0, 0, 59, 0, 98, 0, 0, 0, 47, 0, 0, 0, 41, 0, 0, 60, 35, 0],
    [150, 18, 0, 0, 0, 0, 0, 0, 78, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0],
    [0, 0, 0, 116, 0, 5, 0, 0, 0, 0, 0, 0, 0, 12, 0, 117, 0, 0, 0, 0],
    [0, 0, 45, 35, 0, 0, 0, 0, 162, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8],
    [0, 0, 0, 0, 0, 0, 41, 0, 0, 0, 0, 0, 80, 67, 0, 0, 0, 0, 0, 62],
    [0, 0, 0, 0, 62, 0, 0, 75, 0, 0, 0, 115, 0, 0, 0, 0, 0, 4, 78, 6],
    [0, 163, 37, 0, 0, 0, 1, 0, 0, 111, 0, 0, 25, 0, 0, 0, 0, 3, 0, 0],
    [0, 92, 26, 0, 0, 0, 0, 0, 0, 0, 0, 92, 0, 0, 0, 0, 0, 0, 0, 40],
    [0, 0, 0, 0, 0, 0, 0, 0, 71, 68, 41, 0, 0, 0, 70, 0, 0, 0, 0, 0],
    [152, 15, 0, 19, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 56, 0, 91, 0, 7],
    [0, 0, 138, 0, 0, 13, 0, 0, 0, 0, 0, 0, 98, 1, 0, 0, 0, 0, 0, 0],
    [46, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 0, 0, 0, 0, 0, 0, 0, 58],
    [0, 0, 0, 0, 4, 0, 41, 0, 0, 0, 110, 0, 0, 95, 0, 0, 0, 0, 0, 0],
    [81, 0, 0, 16, 0, 0, 75, 0, 52, 100, 0, 0, 16, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 21, 0, 0, 0, 0, 0, 0, 0, 64, 46, 0, 0, 0, 0, 0, 119, 0],
    [0, 0, 0, 0, 0, 0, 0, 104, 0, 39, 0, 104, 0, 3, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 99, 0, 0, 0, 0, 0, 0, 26, 0, 0, 57, 68, 0, 0, 0],
    [0, 0, 41, 0, 0, 0, 0, 123, 0, 0, 0, 23, 0, 0, 0, 0, 0, 63, 0, 0],
    [0, 0, 0, 177, 0, 0, 0, 37, 0, 0, 73, 12, 0, 0, 0, 0, 0, 0, 26, 15],
    [57, 0, 0, 0, 140, 0, 0, 60, 0, 0, 16, 67, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 16, 0, 0, 0, 29, 142, 0, 71, 34, 0, 0, 0, 48, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 67, 0, 0, 53, 29, 0, 0, 0, 0, 0, 101, 0, 0, 0, 0],
    [81, 0, 0, 0, 22, 0, 0, 0, 0, 0, 0, 0, 20, 0, 0, 0, 127, 0, 0, 0],
    [0, 0, 14, 0, 0, 0, 0, 102, 47, 0, 0, 0, 0, 0, 0, 87, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 55, 0, 0, 0, 119, 0, 0, 65, 0, 0, 0, 0, 11, 0, 0],
    [41, 0, 40, 0, 0, 0, 0, 96, 51, 23, 0, 0, 0, 89, 0, 0, 0, 0, 0, 0],
    [38, 0, 0, 0, 0, 0, 0, 147, 0, 5, 86, 39, 0, 0, 25, 0, 0, 0, 0, 0],
    [4, 0, 0, 89, 0, 0, 0, 0, 50, 0, 118, 0, 72, 0, 7, 0, 0, 0, 0, 0],
    [0, 0, 56, 0, 0, 0, 0, 0, 0, 0, 9, 16, 58, 34, 0, 0, 0, 0, 0, 167],
    [0, 0, 6, 0, 20, 70, 0, 0, 0, 212, 0, 0, 10, 0, 22, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 96, 77, 0, 0, 0, 0, 0, 0, 17, 60],
    [0, 114, 63, 0, 0, 4, 0, 0, 13, 0, 0, 0, 0, 0, 73, 0, 0, 0, 0, 73],
    [0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 25, 0, 0, 69, 118, 0, 122, 0],
    [0, 0, 0, 0, 0, 0, 17, 0, 157, 17, 0, 9, 111, 0, 0, 29, 0, 0, 0, 0],
    [0, 89, 0, 0, 0, 0, 23, 68, 0, 85, 29, 0, 0, 0, 0, 0, 46, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 41, 0, 0, 0, 82, 0, 66, 0, 0, 0, 61, 0, 0],
    [75, 16, 0, 0, 0, 0, 72, 116, 0, 0, 56, 0, 0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 64, 0, 0, 11, 0, 55, 0, 0, 120, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

_outbound_truck_raw_data = [
    [7, 24, 5, 17, 22, 1, 1, 0, 22, 4, 1, 1, 7, 7, 5, 5, 9, 4, 9, 1],
    [6, 4, 14, 6, 19, 4, 2, 14, 5, 0, 9, 23, 3, 27, 7, 3, 1, 5, 0, 2],
    [21, 7, 0, 3, 0, 13, 1, 28, 12, 18, 5, 20, 13, 8, 2, 26, 7, 4, 11, 2],
    [14, 11, 22, 2, 2, 13, 3, 3, 24, 1, 16, 8, 5, 11, 36, 2, 2, 6, 5, 9],
    [9, 2, 3, 3, 43, 17, 12, 2, 0, 4, 14, 3, 16, 3, 2, 6, 3, 5, 1, 0],
    [19, 1, 2, 8, 8, 2, 5, 1, 9, 7, 1, 26, 7, 1, 5, 12, 13, 15, 2, 15],
    [5, 9, 37, 13, 1, 12, 1, 3, 4, 9, 9, 18, 17, 0, 4, 3, 3, 1, 4, 0],
    [14, 3, 23, 17, 13, 5, 1, 28, 0, 0, 1, 14, 0, 6, 1, 2, 7, 24, 3, 9],
    [17, 13, 0, 9, 2, 1, 7, 4, 38, 4, 19, 24, 3, 4, 22, 24, 10, 14, 8, 3],
    [4, 22, 3, 3, 2, 2, 2, 11, 0, 26, 0, 1, 18, 1, 3, 7, 2, 36, 4, 23],
    [2, 16, 7, 5, 6, 24, 13, 4, 2, 26, 67, 17, 49, 7, 21, 4, 16, 4, 5, 21],
    [49, 23, 3, 5, 5, 4, 6, 19, 2, 32, 34, 3, 19, 7, 0, 27, 2, 2, 5, 6],
    [4, 4, 8, 17, 0, 27, 5, 5, 5, 4, 7, 7, 1, 2, 28, 8, 3, 3, 9, 1],
    [2, 3, 15, 9, 0, 5, 7, 6, 23, 21, 0, 9, 20, 16, 10, 6, 0, 26, 1, 5],
    [0, 1, 0, 11, 3, 3, 8, 4, 15, 1, 17, 11, 1, 8, 2, 6, 7, 1, 25, 5],
    [3, 6, 3, 3, 32, 11, 10, 7, 5, 40, 7, 4, 0, 22, 7, 14, 2, 22, 0, 14],
    [2, 9, 22, 3, 3, 1, 2, 2, 12, 4, 47, 1, 16, 8, 14, 9, 6, 2, 6, 13],
    [5, 11, 5, 1, 5, 3, 3, 23, 4, 1, 53, 6, 4, 11, 3, 1, 6, 12, 2, 8],
    [14, 3, 2, 8, 13, 1, 10, 1, 1, 9, 13, 10, 0, 10, 10, 12, 0, 55, 1, 8],
    [1, 3, 9, 0, 1, 9, 16, 9, 2, 12, 7, 29, 15, 5, 16, 2, 6, 1, 25, 4],
    [2, 3, 17, 16, 4, 0, 0, 10, 5, 11, 7, 3, 3, 8, 45, 4, 4, 20, 13, 1],
    [8, 2, 10, 9, 21, 12, 26, 57, 4, 4, 0, 4, 5, 1, 2, 5, 4, 7, 3, 5],
    [3, 0, 2, 8, 2, 8, 31, 2, 2, 2, 9, 6, 3, 36, 1, 6, 6, 6, 1, 39],
    [31, 2, 2, 4, 2, 9, 4, 6, 0, 14, 11, 5, 2, 10, 5, 8, 12, 3, 8, 5],
    [30, 3, 2, 3, 6, 1, 12, 20, 12, 13, 19, 2, 5, 2, 3, 29, 1, 0, 7, 13],
    [12, 5, 6, 3, 7, 5, 1, 5, 7, 2, 32, 5, 4, 14, 2, 1, 17, 6, 2, 4],
    [12, 4, 3, 2, 2, 1, 0, 5, 8, 10, 4, 0, 29, 7, 3, 8, 1, 1, 22, 3],
    [7, 3, 10, 11, 7, 15, 4, 13, 5, 3, 19, 6, 27, 10, 4, 17, 2, 0, 7, 33],
    [9, 1, 1, 14, 4, 3, 12, 23, 0, 14, 7, 28, 3, 15, 0, 2, 2, 17, 0, 10],
    [13, 24, 3, 2, 1, 2, 5, 1, 35, 10, 22, 4, 4, 1, 11, 9, 6, 1, 3, 4],
    [14, 2, 6, 7, 1, 2, 7, 18, 6, 13, 30, 5, 1, 1, 12, 3, 3, 12, 3, 7],
    [8, 1, 5, 4, 6, 7, 5, 5, 11, 17, 8, 4, 3, 1, 1, 5, 2, 10, 12, 8],
    [2, 17, 13, 5, 1, 10, 9, 3, 1, 1, 28, 2, 3, 10, 5, 1, 1, 2, 3, 1],
    [1, 4, 24, 7, 11, 11, 6, 7, 7, 5, 0, 17, 1, 18, 3, 10, 16, 3, 18, 0],
    [6, 7, 5, 3, 3, 8, 4, 5, 3, 1, 6, 13, 8, 7, 6, 5, 4, 1, 10, 6],
    [21, 25, 8, 3, 3, 1, 2, 24, 13, 2, 13, 3, 6, 18, 6, 8, 9, 8, 3, 23],
    [12, 4, 15, 3, 1, 3, 36, 2, 24, 5, 10, 19, 18, 3, 7, 27, 0, 11, 8, 3],
    [28, 19, 6, 1, 3, 17, 3, 7, 6, 4, 6, 14, 6, 17, 5, 0, 5, 6, 1, 2],
    [23, 0, 12, 3, 44, 4, 1, 1, 25, 57, 14, 3, 6, 7, 6, 9, 1, 1, 12, 1],
    [3, 8, 5, 6, 14, 0, 5, 27, 7, 56, 43, 9, 8, 32, 13, 5, 2, 10, 2, 6],
    [26, 3, 6, 14, 9, 15, 1, 8, 22, 1, 37, 3, 7, 3, 6, 4, 0, 1, 0, 5],
    [11, 18, 3, 3, 15, 7, 2, 3, 7, 5, 17, 0, 4, 8, 14, 4, 2, 21, 15, 9],
    [31, 1, 4, 12, 0, 2, 1, 19, 31, 1, 41, 3, 2, 1, 1, 13, 1, 15, 3, 3],
    [17, 49, 1, 1, 3, 12, 1, 17, 18, 2, 6, 21, 6, 3, 0, 10, 4, 5, 6, 1],
    [23, 19, 13, 3, 9, 10, 1, 13, 7, 3, 7, 13, 26, 3, 0, 2, 5, 15, 13, 1],
    [12, 19, 7, 6, 1, 0, 0, 31, 2, 11, 2, 0, 5, 9, 17, 2, 4, 3, 10, 11],
    [15, 40, 7, 6, 15, 4, 11, 12, 11, 12, 33, 1, 8, 3, 3, 20, 9, 3, 4, 12],
    [2, 1, 8, 2, 16, 37, 8, 7, 3, 4, 2, 1, 4, 3, 27, 10, 5, 1, 5, 17],
    [8, 8, 31, 4, 12, 6, 2, 11, 2, 14, 24, 9, 6, 5, 2, 3, 4, 11, 30, 10],
    [3, 1, 3, 1, 2, 6, 2, 38, 6, 2, 24, 4, 2, 7, 17, 32, 3, 6, 3, 12],
    [3, 12, 9, 5, 4, 1, 20, 8, 2, 28, 44, 3, 1, 2, 12, 7, 8, 1, 13, 8],
    [2, 3, 21, 13, 5, 7, 17, 21, 11, 3, 1, 2, 3, 2, 13, 9, 1, 4, 6, 34],
    [13, 2, 7, 3, 21, 14, 1, 10, 9, 1, 31, 2, 3, 9, 15, 8, 2, 2, 19, 16],
    [9, 1, 2, 14, 7, 17, 12, 16, 11, 1, 38, 5, 7, 8, 2, 8, 6, 26, 10, 16],
    [9, 2, 20, 6, 7, 5, 8, 18, 2, 0, 8, 15, 7, 1, 9, 3, 1, 3, 4, 2],
    [11, 10, 0, 1, 3, 12, 5, 1, 24, 2, 8, 1, 2, 6, 4, 5, 18, 13, 2, 3],
    [12, 2, 3, 3, 15, 2, 7, 10, 11, 2, 6, 4, 2, 4, 4, 9, 16, 2, 1, 5],
    [5, 8, 2, 11, 3, 7, 1, 9, 20, 12, 23, 12, 2, 16, 10, 2, 2, 0, 9, 4],
    [5, 2, 5, 1, 8, 1, 3, 4, 1, 2, 3, 18, 5, 1, 7, 6, 5, 4, 2, 11],
    [3, 8, 11, 19, 4, 12, 25, 1, 9, 3, 47, 11, 2, 22, 5, 2, 1, 0, 7, 29],
    [8, 2, 1, 4, 50, 4, 0, 11, 4, 34, 11, 11, 14, 2, 3, 3, 2, 10, 1, 7],
    [5, 8, 14, 8, 0, 8, 9, 2, 5, 32, 1, 33, 5, 4, 8, 2, 21, 1, 34, 6],
    [8, 2, 30, 0, 13, 1, 1, 17, 9, 20, 17, 6, 0, 2, 1, 6, 3, 1, 2, 1],
    [5, 1, 1, 9, 5, 21, 3, 9, 12, 3, 10, 7, 6, 33, 10, 16, 6, 10, 2, 13],
    [3, 11, 4, 8, 11, 12, 2, 3, 16, 8, 0, 1, 5, 3, 5, 20, 27, 18, 4, 3],
    [9, 2, 5, 2, 9, 3, 1, 2, 1, 2, 39, 3, 2, 2, 13, 2, 5, 10, 2, 5],
    [1, 1, 9, 16, 4, 5, 1, 24, 3, 14, 18, 8, 7, 7, 2, 7, 2, 3, 22, 20],
    [4, 9, 0, 4, 1, 2, 1, 32, 2, 1, 14, 10, 14, 3, 2, 5, 0, 6, 11, 15],
    [2, 16, 9, 3, 6, 10, 9, 12, 0, 4, 43, 24, 17, 6, 1, 1, 0, 7, 3, 11],
    [3, 5, 17, 5, 11, 7, 6, 7, 9, 18, 2, 2, 2, 16, 0, 16, 2, 57, 3, 11],
    [1, 12, 5, 1, 2, 2, 16, 1, 6, 45, 18, 0, 26, 3, 22, 18, 11, 4, 11, 3],
    [0, 20, 1, 2, 0, 4, 2, 8, 9, 9, 1, 8, 4, 4, 9, 11, 1, 47, 10, 9],
    [1, 2, 6, 4, 3, 4, 13, 17, 3, 14, 2, 14, 4, 1, 6, 2, 10, 15, 2, 5],
    [13, 12, 31, 2, 0, 1, 2, 2, 3, 19, 7, 39, 5, 15, 3, 39, 2, 4, 3, 4],
    [13, 5, 3, 2, 2, 4, 7, 4, 12, 8, 6, 17, 4, 4, 1, 3, 23, 0, 22, 5],
    [7, 2, 11, 5, 1, 1, 14, 9, 3, 2, 20, 14, 25, 23, 8, 8, 1, 10, 3, 4],
    [29, 0, 1, 10, 25, 15, 3, 30, 4, 14, 5, 27, 20, 21, 0, 0, 12, 23, 3, 0],
    [4, 2, 10, 4, 4, 18, 4, 25, 3, 4, 11, 4, 8, 3, 14, 11, 3, 12, 6, 6],
    [9, 1, 6, 2, 1, 4, 22, 27, 1, 8, 18, 8, 2, 7, 2, 1, 5, 14, 27, 4],
    [2, 3, 1, 1, 6, 5, 5, 48, 24, 2, 11, 5, 9, 0, 22, 2, 11, 1, 7, 14],
    [2, 29, 20, 1, 16, 7, 4, 31, 12, 17, 3, 11, 1, 3, 6, 3, 15, 46, 2, 8],
    [4, 3, 20, 0, 7, 5, 6, 3, 28, 17, 8, 3, 1, 2, 1, 3, 2, 21, 15, 7],
    [4, 7, 8, 4, 4, 1, 0, 11, 14, 2, 2, 11, 52, 2, 3, 4, 1, 0, 5, 15],
    [4, 1, 2, 19, 11, 2, 3, 22, 6, 8, 14, 8, 2, 16, 12, 2, 1, 9, 14, 1],
    [21, 6, 25, 13, 4, 2, 1, 2, 1, 1, 1, 3, 1, 15, 5, 1, 5, 24, 6, 11],
    [9, 3, 8, 2, 7, 3, 5, 6, 28, 6, 6, 16, 22, 14, 13, 20, 2, 2, 2, 3],
    [11, 0, 13, 1, 12, 3, 8, 10, 9, 20, 7, 8, 3, 2, 0, 4, 2, 6, 9, 9],
    [3, 2, 18, 6, 2, 35, 5, 17, 3, 14, 11, 2, 12, 13, 12, 19, 8, 1, 28, 6],
    [14, 7, 10, 8, 1, 3, 5, 2, 7, 2, 23, 3, 6, 6, 1, 2, 9, 1, 1, 1],
    [22, 8, 24, 17, 1, 3, 2, 17, 6, 18, 12, 4, 3, 8, 22, 7, 1, 1, 12, 2],
    [3, 12, 4, 6, 7, 4, 5, 13, 0, 4, 19, 5, 1, 5, 1, 4, 10, 17, 21, 19],
    [4, 4, 0, 7, 9, 1, 7, 2, 7, 4, 18, 25, 38, 5, 23, 17, 0, 1, 13, 15],
    [7, 6, 28, 1, 3, 4, 11, 2, 34, 23, 22, 28, 2, 3, 6, 1, 8, 4, 8, 13],
    [10, 12, 9, 11, 1, 3, 13, 0, 27, 6, 4, 5, 6, 12, 2, 24, 0, 1, 11, 1],
    [3, 5, 44, 3, 17, 10, 8, 4, 9, 5, 30, 19, 1, 8, 6, 12, 4, 2, 0, 21],
    [0, 1, 13, 8, 4, 3, 2, 15, 3, 27, 7, 17, 4, 19, 2, 5, 1, 21, 8, 23],
    [24, 6, 16, 1, 3, 18, 5, 24, 1, 6, 19, 1, 1, 2, 5, 0, 4, 1, 3, 1],
    [30, 1, 1, 3, 2, 14, 3, 12, 8, 4, 29, 7, 1, 7, 0, 6, 5, 9, 22, 3],
    [12, 1, 8, 9, 10, 2, 1, 27, 12, 23, 23, 24, 1, 6, 4, 9, 2, 2, 2, 11],
    [30, 1, 5, 4, 4, 3, 6, 8, 7, 6, 14, 4, 8, 0, 12, 5, 13, 0, 11, 19],
    [32, 2, 22, 3, 13, 4, 0, 8, 6, 5, 7, 2, 5, 3, 1, 1, 16, 9, 22, 31],
    [10, 8, 2, 1, 4, 3, 4, 7, 2, 8, 1, 25, 1, 1, 2, 3, 12, 3, 6, 0],
    [26, 9, 12, 19, 28, 1, 0, 5, 1, 9, 4, 26, 4, 2, 1, 28, 4, 9, 1, 18],
    [40, 5, 17, 7, 1, 20, 1, 6, 1, 8, 19, 8, 11, 4, 0, 3, 4, 39, 4, 8],
    [11, 7, 26, 15, 10, 7, 8, 3, 15, 1, 7, 5, 14, 7, 4, 17, 1, 6, 21, 29],
    [19, 6, 9, 1, 6, 7, 2, 5, 14, 3, 2, 5, 4, 6, 12, 2, 16, 13, 17, 8],
    [15, 2, 4, 1, 27, 0, 1, 5, 25, 7, 5, 16, 9, 19, 11, 19, 1, 4, 17, 1],
    [3, 13, 10, 1, 8, 0, 5, 1, 4, 1, 8, 11, 6, 14, 5, 32, 11, 6, 9, 9],
    [9, 0, 7, 3, 7, 5, 4, 18, 25, 5, 19, 2, 8, 35, 8, 11, 1, 1, 28, 8],
    [21, 8, 0, 3, 6, 2, 0, 10, 4, 4, 1, 17, 7, 7, 9, 6, 17, 27, 19, 28],
    [4, 15, 1, 1, 8, 0, 18, 3, 10, 1, 3, 4, 2, 3, 3, 7, 2, 5, 4, 12],
    [9, 5, 4, 12, 9, 1, 0, 0, 8, 3, 12, 3, 3, 1, 9, 8, 1, 25, 1, 5],
    [20, 32, 3, 1, 1, 5, 19, 1, 1, 36, 28, 8, 19, 18, 3, 2, 2, 10, 10, 21],
    [22, 7, 13, 0, 7, 0, 2, 24, 9, 2, 5, 20, 4, 4, 4, 3, 10, 34, 3, 3],
    [9, 0, 29, 0, 6, 4, 1, 10, 3, 4, 2, 21, 12, 1, 7, 6, 0, 1, 16, 13],
    [31, 8, 21, 6, 20, 6, 7, 1, 18, 5, 18, 2, 0, 2, 2, 32, 11, 8, 10, 30],
    [6, 9, 12, 4, 3, 2, 1, 6, 6, 0, 2, 7, 3, 10, 1, 22, 6, 12, 1, 2],
    [1, 9, 9, 4, 6, 5, 3, 4, 5, 13, 28, 10, 3, 36, 1, 24, 1, 1, 9, 7],
    [20, 32, 6, 10, 5, 10, 7, 18, 6, 2, 10, 7, 15, 7, 12, 4, 18, 14, 3, 8],
    [5, 30, 2, 2, 0, 5, 16, 103, 1, 7, 3, 6, 1, 7, 13, 1, 5, 1, 3, 4],
    [9, 1, 12, 27, 24, 2, 15, 34, 1, 10, 99, 42, 10, 23, 4, 1, 2, 6, 3, 7],
    [3, 0, 23, 22, 5, 26, 1, 14, 30, 5, 4, 8, 10, 6, 5, 19, 22, 3, 6, 5],
    [6, 17, 6, 6, 8, 7, 5, 5, 15, 1, 4, 2, 7, 3, 2, 3, 9, 8, 9, 10],
    [6, 9, 9, 4, 14, 7, 0, 37, 10, 9, 8, 2, 7, 9, 17, 9, 2, 5, 2, 2],
    [29, 2, 6, 2, 8, 4, 3, 49, 11, 3, 4, 3, 1, 13, 46, 17, 3, 14, 54, 39],
    [32, 13, 22, 4, 2, 6, 8, 3, 11, 5, 2, 12, 18, 3, 5, 1, 4, 15, 6, 23],
    [6, 1, 6, 1, 2, 13, 5, 11, 9, 1, 12, 18, 2, 3, 4, 4, 1, 9, 4, 12],
    [35, 9, 3, 0, 3, 1, 3, 15, 15, 29, 25, 8, 9, 6, 3, 20, 8, 7, 1, 40],
    [3, 1, 7, 2, 2, 0, 17, 3, 30, 34, 8, 23, 9, 5, 1, 3, 2, 14, 1, 32],
    [1, 15, 16, 16, 23, 2, 9, 23, 7, 14, 3, 23, 1, 2, 5, 10, 6, 2, 7, 23],
    [0, 1, 2, 10, 20, 3, 2, 11, 13, 0, 3, 26, 4, 7, 2, 0, 9, 9, 22, 6],
    [6, 6, 5, 20, 10, 6, 1, 3, 14, 7, 2, 5, 8, 6, 7, 10, 1, 8, 12, 4],
    [17, 6, 8, 3, 7, 4, 6, 28, 18, 2, 2, 2, 9, 4, 1, 9, 0, 4, 2, 7],
    [3, 21, 8, 8, 10, 1, 2, 5, 3, 7, 3, 0, 14, 4, 16, 0, 12, 3, 2, 6],
    [3, 0, 8, 5, 6, 8, 0, 0, 9, 9, 2, 9, 25, 37, 1, 1, 0, 0, 15, 1],
    [0, 1, 3, 2, 7, 5, 27, 8, 0, 3, 5, 21, 2, 3, 3, 16, 23, 9, 10, 3],
    [5, 2, 3, 7, 25, 2, 5, 2, 1, 4, 23, 21, 13, 0, 12, 9, 6, 1, 12, 1],
    [5, 9, 13, 13, 0, 3, 33, 37, 15, 1, 5, 44, 19, 7, 3, 4, 4, 0, 7, 6],
    [4, 1, 0, 3, 1, 5, 13, 12, 7, 2, 40, 9, 5, 4, 1, 1, 1, 21, 2, 25],
    [16, 13, 2, 18, 12, 27, 0, 10, 7, 6, 52, 9, 1, 6, 9, 18, 14, 0, 9, 50],
    [9, 2, 6, 15, 19, 1, 6, 6, 1, 9, 6, 2, 5, 24, 2, 9, 6, 21, 5, 1],
    [4, 17, 27, 4, 1, 12, 6, 25, 2, 16, 2, 11, 15, 14, 2, 6, 2, 0, 5, 2],
    [34, 4, 3, 5, 2, 5, 2, 7, 10, 3, 11, 0, 4, 1, 13, 4, 0, 43, 4, 13],
    [40, 1, 6, 2, 14, 2, 9, 18, 12, 6, 2, 7, 9, 4, 2, 8, 10, 1, 3, 16],
    [14, 13, 4, 1, 7, 7, 13, 4, 2, 0, 5, 5, 2, 3, 29, 2, 1, 9, 1, 16],
    [1, 13, 5, 2, 3, 9, 6, 3, 2, 2, 15, 8, 1, 11, 10, 1, 7, 15, 5, 5],
    [47, 6, 47, 1, 1, 2, 6, 33, 5, 8, 11, 2, 1, 2, 5, 13, 16, 7, 19, 10],
    [10, 12, 1, 0, 16, 2, 8, 7, 0, 4, 14, 10, 13, 16, 20, 0, 5, 25, 12, 17],
    [6, 2, 34, 6, 1, 2, 4, 22, 6, 27, 20, 3, 9, 4, 32, 8, 1, 4, 7, 1],
    [5, 2, 1, 8, 1, 5, 19, 48, 6, 12, 49, 7, 1, 8, 4, 6, 3, 1, 10, 14],
]

# Derived data.
inbound_truck_count = len(_inbound_truck_raw_data)
outbound_truck_count = len(_outbound_truck_raw_data)
total_truck_count = inbound_truck_count + outbound_truck_count
