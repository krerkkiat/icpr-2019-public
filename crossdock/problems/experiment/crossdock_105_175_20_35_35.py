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
inbound_gate_count = 35
outbound_gate_count = 35

# Parameters used to generate this data.
number_of_total_product_types = 20
product_per_truck_rate = 0.35
possible_inbound_total_product = [250, 340]

# Truck data.
_inbound_truck_raw_data = [
    [0, 96, 0, 0, 0, 0, 0, 0, 48, 0, 0, 18, 0, 0, 0, 0, 0, 88, 0, 0],
    [0, 18, 0, 27, 0, 0, 0, 0, 49, 0, 0, 0, 0, 0, 156, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 3, 0, 97, 0, 0, 219, 12, 1],
    [0, 0, 0, 0, 0, 0, 0, 78, 0, 59, 0, 33, 80, 0, 0, 0, 0, 0, 0, 0],
    [0, 145, 0, 0, 0, 0, 12, 0, 16, 0, 77, 14, 0, 0, 0, 0, 0, 0, 76, 0],
    [0, 0, 4, 0, 0, 0, 0, 0, 162, 0, 0, 63, 0, 0, 0, 0, 0, 21, 0, 0],
    [0, 0, 0, 0, 0, 0, 219, 7, 65, 8, 38, 0, 0, 0, 3, 0, 0, 0, 0, 0],
    [13, 0, 119, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 114, 0, 0, 0, 0],
    [0, 18, 39, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 187, 0, 0, 0, 0, 0],
    [0, 0, 136, 65, 0, 0, 0, 0, 0, 2, 0, 47, 0, 0, 0, 0, 0, 0, 0, 0],
    [52, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 46, 0, 0, 0, 0, 44, 108],
    [0, 0, 0, 70, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 147, 0, 0, 0, 30, 3],
    [0, 34, 0, 0, 0, 0, 0, 0, 41, 0, 0, 0, 49, 0, 41, 68, 107, 0, 0, 0],
    [0, 0, 0, 36, 0, 0, 0, 0, 0, 0, 75, 0, 0, 0, 102, 0, 0, 37, 0, 0],
    [0, 0, 23, 0, 0, 0, 0, 0, 0, 18, 0, 0, 0, 51, 0, 158, 0, 0, 0, 0],
    [0, 0, 0, 30, 0, 0, 0, 0, 0, 0, 0, 0, 80, 0, 0, 3, 0, 51, 8, 168],
    [0, 0, 0, 0, 69, 0, 0, 0, 43, 0, 40, 0, 0, 0, 0, 0, 98, 0, 0, 0],
    [0, 0, 0, 121, 0, 8, 134, 0, 0, 0, 0, 31, 0, 0, 0, 0, 45, 0, 0, 1],
    [0, 0, 38, 0, 42, 0, 0, 0, 0, 21, 0, 0, 148, 0, 75, 0, 0, 16, 0, 0],
    [0, 59, 0, 0, 139, 0, 46, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0],
    [0, 0, 0, 67, 0, 0, 0, 0, 31, 0, 0, 0, 51, 0, 0, 0, 0, 101, 0, 0],
    [69, 51, 0, 0, 0, 106, 0, 8, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 105],
    [112, 0, 26, 50, 0, 0, 0, 0, 82, 0, 0, 0, 0, 0, 32, 0, 0, 0, 0, 38],
    [0, 3, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 36, 32, 0, 0, 238, 0, 28],
    [88, 5, 0, 0, 0, 0, 0, 0, 0, 0, 20, 0, 0, 0, 0, 137, 0, 0, 0, 0],
    [56, 139, 0, 0, 0, 0, 0, 0, 18, 0, 0, 0, 0, 0, 0, 0, 0, 37, 0, 0],
    [0, 0, 0, 95, 0, 0, 0, 102, 0, 0, 0, 0, 29, 0, 24, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 26, 0, 0, 0, 0, 0, 0, 0, 0, 0, 70, 97, 0, 0, 0, 57],
    [0, 0, 0, 0, 0, 0, 0, 145, 44, 0, 0, 0, 28, 0, 33, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 34, 0, 40, 0, 66, 0, 110, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 97, 0, 95, 29, 47, 0, 59, 0, 0, 0, 13, 0, 0, 0, 0, 0, 0],
    [14, 0, 0, 0, 0, 33, 0, 0, 47, 0, 0, 0, 0, 0, 74, 0, 22, 0, 0, 150],
    [0, 0, 0, 0, 0, 0, 75, 72, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 99],
    [37, 28, 14, 0, 0, 0, 0, 0, 0, 13, 0, 0, 0, 21, 0, 0, 0, 227, 0, 0],
    [0, 0, 62, 0, 0, 0, 0, 14, 0, 0, 0, 0, 97, 0, 0, 0, 77, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 2, 0, 33, 0, 0, 103, 44, 0, 0, 0, 122, 0, 0, 36],
    [0, 0, 0, 0, 21, 0, 0, 0, 0, 0, 122, 7, 0, 154, 25, 0, 0, 0, 0, 11],
    [18, 0, 23, 0, 0, 0, 0, 95, 0, 0, 0, 0, 0, 0, 0, 114, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 28, 0, 0, 27, 0, 10, 0, 0, 185, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 182, 5, 44, 19, 0, 0, 0, 0],
    [10, 0, 0, 0, 0, 0, 0, 2, 32, 0, 0, 22, 129, 0, 0, 0, 0, 0, 0, 145],
    [0, 79, 0, 0, 18, 175, 0, 0, 0, 0, 0, 64, 2, 0, 0, 0, 0, 0, 0, 2],
    [0, 0, 17, 0, 0, 0, 0, 57, 149, 0, 0, 0, 0, 0, 0, 27, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 2, 8, 0, 33, 0, 0, 0, 45, 0, 1, 251, 0, 0, 0],
    [0, 23, 0, 12, 36, 0, 0, 142, 0, 0, 0, 0, 0, 0, 31, 0, 0, 0, 96, 0],
    [0, 0, 0, 0, 0, 0, 58, 69, 0, 47, 0, 17, 0, 0, 0, 38, 111, 0, 0, 0],
    [0, 0, 124, 0, 0, 0, 0, 0, 0, 0, 84, 0, 0, 0, 0, 0, 27, 0, 0, 15],
    [0, 0, 0, 0, 26, 0, 0, 80, 0, 0, 0, 0, 0, 0, 98, 0, 116, 2, 0, 18],
    [18, 0, 0, 0, 164, 0, 0, 0, 0, 0, 68, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 5, 0, 0, 0, 69, 0, 0, 0, 0, 1, 0, 0, 0, 191, 36, 38, 0, 0, 0],
    [15, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 246, 0, 0, 0, 35, 0, 41, 0],
    [168, 0, 0, 0, 0, 43, 5, 0, 72, 0, 0, 0, 44, 8, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 121, 0, 40, 56, 52, 63, 0, 0, 0],
    [0, 0, 0, 12, 54, 0, 0, 11, 59, 66, 0, 0, 0, 0, 0, 0, 0, 0, 0, 138],
    [0, 29, 0, 199, 0, 28, 0, 0, 0, 0, 6, 0, 0, 0, 0, 44, 0, 34, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 83, 16, 0, 0, 19, 0, 0, 0, 132, 0],
    [0, 8, 0, 14, 0, 0, 60, 0, 0, 120, 0, 104, 0, 0, 0, 0, 34, 0, 0, 0],
    [0, 0, 0, 3, 0, 103, 0, 9, 138, 0, 0, 0, 0, 0, 7, 0, 0, 0, 80, 0],
    [0, 0, 0, 0, 184, 0, 12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 34, 20],
    [0, 0, 0, 0, 0, 0, 0, 0, 190, 0, 0, 0, 53, 0, 0, 5, 0, 0, 0, 2],
    [0, 0, 0, 110, 0, 74, 31, 0, 56, 0, 0, 0, 0, 0, 0, 0, 0, 52, 0, 17],
    [0, 0, 0, 36, 0, 63, 0, 0, 0, 0, 45, 0, 0, 0, 0, 0, 106, 0, 0, 0],
    [13, 0, 43, 0, 47, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 147, 0],
    [0, 235, 0, 0, 0, 0, 0, 40, 11, 0, 15, 0, 0, 0, 0, 0, 0, 38, 1, 0],
    [0, 0, 0, 24, 0, 0, 0, 62, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 21, 143],
    [0, 0, 124, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 95, 0, 0, 22, 0, 9, 0],
    [0, 0, 43, 41, 0, 0, 0, 0, 0, 0, 70, 0, 96, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 4, 94, 0, 0, 0, 80, 0, 0, 0, 0, 0, 0, 10, 145, 7, 0, 0, 0],
    [0, 0, 37, 0, 152, 0, 55, 0, 0, 0, 0, 0, 0, 2, 0, 60, 0, 0, 34, 0],
    [0, 0, 0, 0, 0, 0, 78, 0, 1, 97, 0, 0, 0, 0, 74, 0, 0, 0, 0, 0],
    [40, 16, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 152, 42, 0],
    [0, 0, 0, 0, 30, 95, 0, 0, 11, 0, 0, 0, 0, 79, 0, 0, 47, 0, 0, 78],
    [0, 0, 0, 0, 0, 0, 151, 0, 0, 31, 0, 0, 0, 0, 0, 6, 0, 0, 62, 0],
    [103, 0, 0, 0, 0, 0, 13, 0, 0, 0, 0, 0, 0, 0, 0, 0, 134, 0, 0, 0],
    [71, 0, 0, 0, 0, 85, 0, 0, 77, 0, 0, 61, 0, 0, 7, 0, 0, 0, 39, 0],
    [0, 101, 0, 96, 0, 10, 0, 0, 0, 0, 0, 0, 0, 43, 0, 0, 0, 0, 0, 0],
    [18, 0, 0, 0, 0, 0, 0, 112, 0, 0, 80, 0, 0, 0, 0, 0, 0, 0, 0, 40],
    [0, 0, 0, 160, 0, 0, 0, 0, 47, 0, 0, 0, 0, 26, 0, 0, 0, 17, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 38, 0, 0, 0, 0, 0, 0, 0, 44, 0, 49, 119],
    [0, 96, 0, 0, 0, 0, 0, 0, 0, 18, 0, 0, 3, 0, 0, 0, 0, 0, 133, 0],
    [0, 39, 0, 0, 0, 0, 0, 3, 0, 76, 0, 0, 104, 32, 0, 0, 0, 86, 0, 0],
    [37, 0, 0, 74, 24, 0, 0, 0, 0, 0, 0, 0, 0, 0, 115, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 35, 0, 0, 55, 0, 33, 1, 0, 0, 0, 116, 0, 0, 0, 0, 100],
    [0, 83, 70, 0, 0, 0, 97, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 72, 0, 11],
    [0, 19, 0, 0, 0, 0, 0, 33, 0, 0, 120, 0, 0, 78, 0, 0, 0, 0, 0, 0],
    [109, 0, 9, 0, 32, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 100, 0, 0],
    [0, 65, 0, 0, 0, 0, 126, 0, 0, 74, 5, 30, 0, 0, 0, 0, 0, 0, 40, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 62, 0, 52, 0, 0, 0, 0, 0, 123, 13, 0, 0],
    [0, 0, 0, 0, 27, 0, 0, 0, 0, 0, 15, 60, 173, 35, 0, 0, 0, 0, 30, 0],
    [10, 0, 0, 34, 0, 0, 0, 0, 127, 0, 0, 132, 0, 8, 0, 29, 0, 0, 0, 0],
    [0, 0, 3, 29, 36, 182, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 157, 41, 0, 0, 0, 0, 2, 0, 0, 0, 0, 50, 0, 0],
    [75, 0, 0, 0, 0, 0, 5, 0, 0, 17, 188, 0, 15, 0, 0, 40, 0, 0, 0, 0],
    [188, 54, 0, 0, 0, 0, 13, 3, 0, 0, 0, 0, 0, 0, 0, 61, 0, 0, 0, 21],
    [0, 104, 0, 23, 0, 14, 0, 136, 0, 0, 0, 0, 0, 0, 24, 0, 39, 0, 0, 0],
    [0, 0, 0, 0, 57, 0, 0, 0, 0, 0, 0, 0, 0, 0, 115, 0, 0, 25, 53, 0],
    [0, 0, 0, 0, 0, 0, 29, 0, 0, 134, 0, 0, 0, 0, 0, 0, 38, 0, 49, 0],
    [0, 0, 15, 0, 0, 0, 21, 27, 0, 79, 0, 0, 0, 0, 173, 25, 0, 0, 0, 0],
    [0, 0, 0, 77, 0, 0, 17, 0, 0, 0, 14, 0, 0, 0, 0, 25, 0, 0, 202, 5],
    [152, 75, 20, 6, 0, 29, 0, 0, 0, 0, 0, 0, 0, 58, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 72, 0, 0, 0, 0, 0, 0, 65, 105, 0, 8, 0],
    [15, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 214, 0, 43, 0, 0, 9, 53, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 23, 0, 42, 0, 136, 0, 0, 0, 0, 49, 0],
    [25, 0, 84, 0, 0, 0, 0, 19, 0, 0, 106, 0, 38, 0, 68, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 80, 0, 0, 0, 23, 128, 0, 103, 0, 0],
]

_outbound_truck_raw_data = [
    [11, 3, 9, 15, 6, 4, 27, 3, 13, 9, 8, 14, 3, 0, 9, 3, 4, 6, 3, 1],
    [7, 0, 0, 2, 5, 7, 20, 3, 17, 1, 3, 0, 3, 4, 54, 11, 20, 17, 9, 2],
    [3, 16, 9, 11, 7, 9, 1, 10, 12, 7, 9, 1, 10, 5, 0, 0, 6, 3, 1, 6],
    [3, 15, 3, 4, 1, 4, 29, 2, 4, 14, 3, 10, 1, 5, 3, 2, 6, 6, 17, 17],
    [10, 3, 7, 8, 14, 1, 0, 1, 8, 8, 20, 3, 28, 9, 9, 15, 18, 3, 2, 1],
    [5, 46, 6, 27, 11, 7, 6, 7, 13, 0, 23, 1, 3, 42, 2, 1, 11, 5, 8, 16],
    [7, 8, 4, 8, 20, 5, 4, 25, 9, 4, 2, 11, 48, 0, 1, 33, 1, 1, 36, 10],
    [19, 1, 1, 12, 8, 20, 6, 4, 19, 6, 1, 5, 48, 1, 12, 14, 1, 25, 11, 7],
    [5, 2, 12, 12, 7, 2, 9, 9, 28, 8, 5, 5, 3, 0, 22, 8, 13, 1, 5, 16],
    [10, 11, 7, 1, 7, 2, 5, 2, 5, 4, 1, 35, 18, 2, 29, 4, 9, 21, 13, 2],
    [11, 17, 7, 7, 4, 19, 8, 40, 24, 5, 0, 7, 18, 6, 17, 3, 4, 3, 3, 5],
    [2, 7, 1, 12, 14, 6, 8, 9, 32, 10, 5, 3, 2, 1, 7, 4, 4, 8, 4, 15],
    [23, 18, 1, 7, 1, 7, 2, 7, 14, 4, 5, 2, 7, 10, 6, 1, 7, 5, 12, 13],
    [4, 13, 1, 20, 38, 2, 5, 1, 13, 1, 8, 8, 5, 8, 4, 2, 5, 6, 3, 4],
    [51, 0, 0, 25, 8, 12, 2, 2, 12, 6, 26, 2, 4, 2, 1, 14, 5, 27, 12, 3],
    [11, 8, 10, 16, 4, 4, 5, 7, 9, 2, 1, 2, 2, 4, 27, 7, 1, 2, 10, 5],
    [4, 1, 3, 1, 7, 2, 7, 1, 19, 1, 5, 6, 3, 0, 5, 36, 22, 6, 5, 1],
    [21, 0, 0, 4, 18, 13, 3, 7, 0, 6, 3, 4, 1, 2, 10, 13, 12, 8, 11, 13],
    [12, 2, 7, 21, 9, 2, 7, 1, 0, 7, 14, 5, 12, 8, 8, 3, 11, 23, 0, 7],
    [6, 10, 5, 3, 4, 12, 5, 42, 33, 2, 9, 5, 5, 2, 2, 9, 0, 19, 1, 1],
    [0, 3, 6, 5, 0, 13, 0, 6, 4, 0, 1, 12, 13, 2, 5, 8, 36, 3, 10, 15],
    [15, 14, 11, 35, 23, 6, 8, 8, 16, 17, 5, 0, 3, 2, 5, 4, 8, 12, 24, 1],
    [0, 5, 16, 38, 3, 9, 1, 6, 25, 1, 4, 4, 14, 20, 6, 9, 29, 8, 27, 7],
    [3, 3, 2, 2, 2, 6, 14, 6, 2, 1, 1, 1, 3, 3, 12, 9, 4, 2, 5, 3],
    [2, 32, 7, 17, 14, 9, 7, 0, 18, 4, 1, 13, 5, 11, 2, 4, 2, 15, 19, 2],
    [26, 11, 3, 9, 1, 2, 7, 4, 9, 1, 2, 8, 3, 2, 8, 7, 6, 14, 6, 2],
    [5, 21, 14, 6, 2, 20, 10, 4, 30, 4, 7, 2, 2, 12, 8, 8, 16, 16, 14, 24],
    [30, 4, 2, 19, 9, 1, 7, 15, 9, 2, 6, 7, 14, 2, 8, 9, 4, 19, 5, 9],
    [12, 25, 2, 12, 14, 3, 1, 16, 8, 6, 8, 3, 6, 7, 7, 0, 36, 5, 2, 1],
    [22, 3, 3, 4, 6, 8, 5, 7, 9, 5, 12, 6, 9, 0, 24, 7, 8, 4, 3, 24],
    [7, 2, 4, 6, 11, 5, 14, 10, 15, 10, 10, 18, 18, 18, 8, 2, 7, 9, 44, 17],
    [1, 0, 14, 21, 18, 18, 3, 4, 7, 11, 5, 2, 26, 3, 3, 3, 1, 7, 0, 9],
    [9, 3, 0, 3, 14, 2, 12, 10, 14, 3, 1, 7, 4, 2, 2, 4, 22, 32, 4, 6],
    [2, 15, 9, 5, 1, 13, 8, 4, 41, 3, 13, 1, 7, 0, 35, 7, 2, 1, 0, 33],
    [3, 19, 6, 2, 1, 26, 2, 0, 3, 7, 18, 7, 1, 9, 1, 0, 29, 49, 13, 3],
    [4, 23, 10, 2, 12, 6, 6, 3, 20, 5, 6, 5, 5, 4, 0, 1, 14, 19, 18, 3],
    [7, 0, 1, 25, 7, 1, 5, 1, 8, 6, 15, 2, 12, 2, 25, 8, 6, 16, 4, 0],
    [2, 2, 13, 17, 1, 3, 3, 2, 0, 3, 4, 25, 9, 5, 3, 36, 6, 7, 3, 61],
    [10, 16, 13, 3, 5, 3, 15, 6, 3, 4, 1, 1, 0, 11, 18, 5, 2, 5, 3, 20],
    [7, 6, 4, 14, 24, 6, 8, 4, 3, 1, 3, 0, 8, 9, 0, 20, 0, 7, 4, 11],
    [8, 10, 5, 5, 2, 9, 14, 17, 54, 0, 6, 3, 2, 13, 26, 0, 35, 3, 6, 2],
    [12, 7, 2, 19, 1, 7, 8, 5, 15, 1, 2, 1, 23, 9, 26, 13, 12, 5, 14, 9],
    [18, 5, 1, 2, 2, 35, 4, 24, 2, 3, 3, 9, 1, 3, 7, 11, 4, 13, 5, 40],
    [5, 15, 26, 7, 2, 10, 3, 11, 15, 1, 21, 2, 2, 0, 40, 8, 9, 12, 4, 2],
    [37, 7, 4, 1, 2, 9, 11, 26, 2, 10, 9, 3, 16, 3, 13, 31, 11, 5, 12, 13],
    [28, 5, 7, 5, 16, 16, 22, 6, 15, 3, 9, 3, 14, 5, 0, 7, 7, 6, 3, 14],
    [4, 35, 14, 2, 8, 4, 4, 7, 10, 3, 8, 8, 9, 6, 1, 22, 20, 2, 1, 10],
    [2, 0, 27, 4, 7, 13, 12, 4, 16, 3, 7, 1, 13, 0, 9, 4, 7, 21, 12, 3],
    [5, 2, 8, 5, 0, 2, 12, 6, 9, 14, 2, 4, 6, 1, 2, 1, 18, 2, 6, 16],
    [2, 17, 2, 1, 0, 15, 1, 1, 0, 9, 15, 3, 21, 2, 16, 6, 13, 5, 4, 6],
    [2, 4, 14, 9, 27, 2, 89, 9, 3, 28, 3, 4, 11, 10, 25, 3, 1, 7, 3, 2],
    [5, 15, 8, 19, 14, 2, 0, 35, 26, 1, 44, 10, 8, 15, 22, 2, 32, 24, 1, 1],
    [52, 4, 0, 3, 5, 2, 6, 3, 12, 8, 20, 0, 17, 1, 15, 1, 0, 3, 18, 4],
    [0, 18, 3, 2, 10, 2, 3, 15, 8, 1, 6, 4, 8, 11, 3, 13, 6, 37, 4, 31],
    [7, 11, 2, 9, 4, 4, 11, 8, 2, 1, 18, 2, 3, 1, 0, 11, 2, 14, 36, 9],
    [22, 13, 7, 5, 1, 2, 19, 6, 4, 15, 5, 8, 7, 1, 5, 9, 1, 10, 18, 5],
    [4, 9, 2, 3, 7, 4, 6, 5, 20, 15, 0, 5, 14, 10, 6, 8, 7, 19, 1, 10],
    [12, 3, 15, 9, 2, 4, 21, 0, 3, 2, 8, 3, 4, 2, 5, 15, 8, 38, 2, 2],
    [10, 1, 6, 5, 15, 15, 2, 1, 8, 13, 11, 12, 18, 19, 14, 9, 14, 2, 3, 25],
    [3, 3, 3, 4, 5, 11, 8, 2, 7, 8, 10, 14, 17, 11, 23, 1, 16, 17, 0, 12],
    [1, 14, 3, 2, 5, 0, 4, 10, 1, 6, 1, 0, 1, 3, 29, 8, 14, 5, 14, 15],
    [1, 4, 11, 3, 1, 8, 16, 5, 2, 2, 8, 8, 6, 6, 3, 3, 7, 1, 4, 15],
    [17, 5, 3, 4, 0, 1, 0, 12, 1, 19, 13, 3, 11, 1, 6, 2, 16, 13, 7, 3],
    [8, 0, 9, 4, 1, 6, 6, 10, 9, 9, 29, 11, 7, 9, 15, 15, 2, 4, 0, 5],
    [0, 3, 5, 25, 6, 2, 35, 8, 14, 4, 2, 7, 10, 2, 26, 2, 6, 28, 13, 4],
    [26, 23, 6, 22, 8, 4, 4, 3, 6, 1, 15, 33, 0, 14, 41, 10, 1, 8, 24, 5],
    [5, 29, 5, 22, 2, 2, 1, 10, 1, 0, 9, 13, 5, 3, 3, 0, 8, 1, 8, 21],
    [1, 9, 2, 6, 6, 3, 1, 1, 9, 5, 13, 1, 1, 11, 1, 1, 12, 2, 5, 1],
    [10, 1, 4, 5, 4, 3, 2, 3, 1, 14, 1, 4, 36, 1, 4, 18, 15, 26, 10, 4],
    [3, 13, 5, 25, 13, 1, 1, 22, 0, 10, 4, 2, 7, 1, 18, 3, 18, 5, 12, 3],
    [2, 3, 21, 9, 12, 6, 2, 1, 35, 0, 9, 25, 2, 2, 19, 1, 1, 8, 5, 6],
    [16, 1, 3, 0, 18, 10, 15, 11, 15, 1, 2, 0, 2, 2, 13, 5, 7, 0, 21, 18],
    [2, 2, 20, 6, 6, 1, 1, 6, 10, 3, 8, 10, 5, 2, 1, 3, 8, 15, 6, 10],
    [0, 18, 6, 10, 12, 25, 12, 7, 4, 1, 1, 9, 8, 5, 19, 0, 32, 2, 6, 5],
    [1, 7, 1, 39, 16, 5, 81, 2, 28, 4, 0, 9, 4, 3, 1, 1, 14, 11, 2, 9],
    [1, 15, 0, 10, 3, 1, 2, 4, 5, 8, 6, 10, 39, 5, 2, 22, 4, 3, 0, 10],
    [10, 7, 11, 2, 0, 6, 16, 7, 11, 2, 9, 14, 4, 6, 26, 9, 5, 14, 1, 1],
    [12, 72, 2, 4, 9, 0, 8, 1, 1, 9, 1, 8, 2, 1, 13, 1, 30, 0, 11, 10],
    [2, 8, 5, 7, 16, 10, 8, 12, 8, 2, 3, 7, 1, 3, 6, 9, 0, 10, 3, 3],
    [2, 3, 1, 2, 4, 1, 9, 1, 22, 4, 11, 0, 9, 0, 8, 5, 13, 64, 9, 22],
    [1, 9, 9, 17, 2, 0, 3, 2, 15, 11, 5, 15, 2, 4, 12, 19, 18, 5, 6, 5],
    [14, 8, 3, 10, 0, 3, 12, 0, 12, 7, 2, 5, 24, 16, 46, 12, 6, 4, 2, 22],
    [4, 23, 2, 4, 2, 2, 3, 7, 20, 17, 4, 1, 4, 7, 3, 21, 14, 7, 4, 5],
    [2, 4, 6, 1, 2, 15, 2, 1, 2, 18, 10, 8, 10, 5, 28, 23, 6, 25, 6, 1],
    [1, 29, 4, 20, 10, 16, 26, 15, 4, 14, 2, 1, 0, 1, 6, 9, 6, 7, 1, 0],
    [2, 6, 0, 33, 6, 0, 11, 0, 1, 4, 27, 29, 13, 1, 9, 7, 0, 2, 14, 4],
    [1, 1, 8, 14, 7, 10, 8, 25, 12, 7, 2, 1, 21, 2, 6, 4, 4, 31, 1, 32],
    [15, 1, 3, 6, 10, 4, 2, 6, 7, 1, 23, 0, 33, 14, 7, 49, 18, 9, 9, 3],
    [13, 8, 3, 12, 4, 1, 2, 1, 18, 26, 1, 19, 10, 12, 12, 11, 11, 15, 8, 20],
    [0, 26, 1, 5, 4, 20, 7, 26, 1, 3, 3, 1, 28, 14, 13, 2, 1, 8, 2, 2],
    [7, 12, 1, 5, 0, 3, 4, 4, 6, 12, 1, 18, 10, 2, 32, 5, 4, 9, 1, 0],
    [11, 6, 6, 13, 6, 0, 5, 0, 11, 22, 9, 4, 17, 8, 12, 10, 5, 5, 10, 4],
    [4, 2, 11, 16, 1, 4, 0, 8, 4, 3, 16, 2, 1, 3, 16, 1, 13, 11, 4, 4],
    [2, 3, 0, 9, 2, 0, 3, 18, 52, 3, 16, 2, 1, 9, 31, 2, 1, 17, 30, 3],
    [7, 16, 17, 9, 16, 13, 3, 5, 4, 1, 19, 23, 4, 20, 15, 16, 5, 3, 9, 8],
    [12, 9, 2, 7, 5, 10, 6, 21, 39, 7, 7, 10, 12, 4, 80, 13, 20, 7, 4, 8],
    [2, 2, 8, 5, 5, 5, 14, 7, 19, 4, 13, 18, 1, 3, 5, 5, 22, 15, 3, 23],
    [11, 2, 1, 3, 15, 11, 6, 1, 1, 1, 28, 2, 10, 11, 12, 4, 5, 2, 10, 5],
    [1, 14, 2, 4, 7, 24, 4, 16, 20, 20, 4, 12, 6, 11, 22, 7, 1, 4, 7, 4],
    [4, 8, 10, 12, 2, 5, 16, 7, 15, 7, 18, 2, 2, 21, 21, 3, 6, 23, 10, 19],
    [14, 6, 12, 10, 2, 3, 2, 3, 19, 17, 7, 1, 20, 30, 3, 6, 4, 1, 16, 2],
    [6, 12, 10, 29, 13, 0, 2, 1, 23, 4, 37, 10, 8, 11, 7, 2, 4, 0, 5, 3],
    [0, 7, 9, 4, 1, 14, 1, 4, 16, 5, 14, 2, 24, 7, 7, 1, 5, 1, 16, 11],
    [9, 3, 4, 11, 9, 9, 0, 21, 9, 1, 4, 9, 6, 0, 15, 4, 15, 12, 6, 8],
    [1, 11, 5, 7, 0, 4, 2, 12, 21, 2, 7, 4, 31, 1, 9, 48, 6, 4, 9, 2],
    [23, 6, 2, 29, 1, 0, 2, 1, 1, 3, 16, 5, 3, 4, 5, 19, 35, 1, 11, 13],
    [5, 1, 1, 7, 4, 2, 3, 4, 1, 3, 11, 5, 3, 5, 10, 1, 23, 9, 5, 14],
    [8, 5, 19, 4, 3, 9, 5, 15, 4, 13, 9, 4, 61, 1, 13, 18, 1, 1, 2, 17],
    [1, 34, 7, 7, 8, 0, 23, 14, 23, 1, 0, 16, 10, 4, 20, 16, 29, 3, 13, 3],
    [9, 19, 3, 10, 6, 5, 4, 3, 24, 5, 21, 3, 6, 7, 8, 3, 5, 10, 15, 35],
    [3, 23, 4, 15, 3, 4, 9, 1, 23, 1, 6, 4, 24, 2, 8, 1, 0, 6, 16, 33],
    [28, 17, 1, 15, 3, 6, 21, 0, 9, 4, 1, 5, 15, 4, 2, 5, 37, 4, 1, 28],
    [1, 1, 5, 5, 5, 17, 8, 15, 1, 6, 1, 15, 5, 4, 14, 2, 2, 7, 6, 1],
    [6, 1, 9, 0, 1, 5, 11, 27, 8, 9, 1, 0, 1, 3, 12, 37, 5, 26, 10, 3],
    [4, 2, 12, 3, 1, 11, 18, 5, 2, 10, 6, 8, 10, 2, 6, 18, 34, 13, 4, 0],
    [20, 3, 2, 1, 19, 0, 8, 4, 3, 6, 1, 3, 8, 4, 3, 7, 8, 5, 13, 0],
    [7, 15, 15, 1, 17, 3, 7, 11, 11, 7, 10, 17, 0, 8, 3, 3, 9, 1, 14, 17],
    [9, 3, 7, 1, 1, 15, 25, 28, 7, 9, 7, 4, 10, 5, 3, 4, 8, 6, 3, 8],
    [7, 3, 3, 0, 15, 22, 3, 8, 0, 2, 66, 3, 28, 2, 7, 14, 9, 3, 9, 12],
    [7, 12, 12, 24, 1, 19, 12, 7, 16, 10, 2, 0, 1, 5, 5, 11, 4, 2, 1, 7],
    [14, 6, 3, 17, 10, 0, 4, 0, 2, 4, 1, 2, 7, 0, 1, 6, 23, 0, 22, 16],
    [1, 1, 1, 19, 17, 8, 1, 19, 13, 9, 12, 5, 2, 2, 16, 6, 7, 14, 4, 15],
    [1, 4, 2, 11, 18, 0, 11, 8, 7, 7, 19, 21, 19, 7, 9, 2, 4, 29, 1, 7],
    [13, 3, 2, 28, 1, 11, 5, 4, 0, 10, 6, 7, 3, 2, 4, 1, 9, 3, 2, 0],
    [28, 11, 12, 23, 9, 8, 2, 9, 18, 6, 19, 14, 1, 1, 18, 0, 11, 5, 9, 7],
    [6, 1, 0, 6, 8, 3, 2, 1, 4, 2, 6, 6, 2, 10, 30, 1, 25, 1, 0, 3],
    [6, 1, 5, 1, 0, 2, 1, 24, 7, 6, 10, 9, 34, 1, 3, 9, 21, 26, 15, 10],
    [2, 6, 4, 1, 1, 2, 3, 11, 2, 3, 18, 34, 0, 4, 19, 56, 0, 8, 3, 25],
    [18, 1, 2, 17, 10, 1, 2, 5, 10, 5, 7, 18, 4, 2, 2, 4, 24, 13, 12, 42],
    [6, 21, 1, 4, 15, 3, 11, 4, 7, 0, 6, 5, 13, 8, 57, 6, 25, 5, 18, 6],
    [1, 6, 3, 12, 16, 1, 3, 0, 53, 10, 7, 8, 9, 6, 5, 17, 1, 9, 0, 8],
    [6, 8, 1, 10, 20, 14, 1, 7, 9, 4, 0, 3, 26, 20, 5, 2, 24, 17, 6, 6],
    [3, 27, 16, 18, 1, 7, 3, 1, 3, 3, 0, 1, 8, 8, 5, 1, 34, 4, 3, 20],
    [25, 2, 5, 1, 0, 6, 13, 14, 1, 10, 2, 1, 3, 1, 21, 8, 29, 15, 2, 21],
    [3, 18, 0, 14, 7, 3, 1, 15, 5, 4, 4, 5, 0, 7, 4, 1, 28, 7, 6, 0],
    [1, 3, 9, 1, 3, 18, 13, 17, 4, 5, 1, 22, 6, 0, 38, 8, 2, 13, 11, 11],
    [6, 0, 3, 3, 19, 25, 6, 6, 2, 1, 0, 3, 15, 3, 2, 3, 5, 0, 21, 4],
    [15, 9, 11, 2, 1, 17, 17, 1, 12, 3, 1, 3, 4, 2, 17, 3, 5, 19, 6, 1],
    [1, 1, 11, 5, 1, 1, 1, 20, 0, 7, 5, 4, 0, 37, 1, 12, 40, 4, 2, 6],
    [3, 0, 0, 19, 7, 6, 4, 22, 1, 4, 9, 2, 45, 3, 3, 1, 8, 29, 15, 21],
    [0, 2, 32, 17, 4, 5, 1, 10, 1, 2, 5, 20, 18, 18, 10, 1, 26, 14, 3, 6],
    [1, 1, 1, 3, 7, 3, 0, 0, 2, 9, 5, 1, 2, 3, 36, 8, 29, 8, 0, 1],
    [3, 5, 4, 3, 10, 11, 17, 11, 29, 3, 10, 2, 2, 3, 4, 27, 8, 28, 3, 2],
    [0, 4, 3, 19, 8, 6, 12, 8, 0, 2, 10, 1, 5, 5, 49, 0, 1, 5, 19, 3],
    [2, 12, 10, 20, 2, 4, 6, 6, 11, 2, 14, 1, 3, 2, 2, 3, 7, 1, 5, 7],
    [32, 30, 14, 3, 0, 15, 8, 12, 15, 26, 9, 4, 6, 1, 2, 4, 37, 6, 6, 29],
    [3, 1, 1, 1, 5, 12, 3, 14, 18, 2, 1, 3, 15, 1, 13, 1, 34, 15, 1, 2],
    [19, 5, 4, 1, 24, 0, 38, 0, 1, 6, 16, 3, 2, 1, 34, 6, 1, 12, 6, 1],
    [2, 20, 5, 3, 2, 8, 14, 6, 1, 1, 3, 3, 17, 8, 3, 11, 10, 3, 15, 6],
    [1, 7, 11, 20, 15, 2, 14, 7, 4, 3, 3, 2, 10, 2, 10, 7, 19, 4, 16, 6],
    [6, 30, 9, 4, 39, 4, 0, 30, 14, 1, 20, 20, 2, 4, 8, 11, 13, 2, 9, 10],
    [8, 4, 1, 25, 4, 8, 2, 1, 15, 4, 4, 20, 4, 0, 12, 14, 3, 38, 8, 4],
    [1, 8, 12, 5, 2, 1, 8, 23, 25, 0, 12, 3, 5, 9, 13, 3, 19, 27, 13, 4],
    [10, 2, 10, 7, 1, 8, 0, 23, 1, 4, 3, 11, 1, 22, 1, 12, 0, 3, 27, 15],
    [0, 7, 3, 10, 8, 1, 4, 5, 6, 3, 9, 16, 19, 5, 23, 1, 3, 12, 26, 11],
    [12, 5, 0, 3, 1, 7, 5, 2, 4, 2, 7, 3, 12, 8, 22, 4, 2, 4, 13, 11],
    [1, 7, 4, 14, 7, 6, 12, 10, 10, 3, 32, 3, 4, 5, 29, 4, 16, 24, 8, 27],
    [1, 6, 14, 15, 6, 11, 8, 4, 11, 6, 7, 2, 2, 12, 58, 5, 32, 21, 33, 3],
    [10, 7, 9, 16, 7, 6, 10, 4, 10, 5, 1, 9, 16, 1, 9, 3, 4, 5, 13, 0],
    [1, 2, 8, 1, 3, 18, 16, 19, 7, 2, 12, 0, 12, 11, 8, 2, 3, 23, 7, 16],
    [2, 4, 3, 28, 4, 10, 33, 39, 1, 8, 15, 5, 1, 0, 19, 25, 4, 17, 13, 6],
    [12, 12, 7, 8, 5, 9, 4, 4, 12, 1, 2, 4, 14, 28, 6, 8, 1, 2, 4, 21],
    [2, 4, 1, 3, 6, 2, 23, 2, 6, 3, 5, 3, 3, 1, 5, 2, 5, 1, 13, 12],
    [4, 0, 1, 5, 1, 5, 13, 5, 2, 13, 7, 10, 17, 0, 1, 3, 0, 10, 28, 1],
    [25, 25, 7, 9, 15, 10, 4, 12, 17, 5, 6, 38, 7, 2, 45, 0, 27, 0, 6, 11],
    [11, 8, 9, 17, 3, 8, 13, 50, 4, 1, 4, 4, 5, 4, 19, 6, 21, 6, 0, 11],
    [29, 6, 1, 34, 5, 0, 3, 6, 0, 1, 0, 13, 2, 7, 7, 2, 9, 11, 6, 0],
    [18, 3, 13, 4, 15, 2, 7, 5, 4, 13, 3, 2, 3, 8, 0, 17, 5, 8, 0, 3],
    [27, 16, 12, 3, 3, 0, 11, 9, 2, 1, 1, 1, 9, 3, 9, 12, 3, 4, 20, 13],
    [6, 28, 6, 7, 3, 26, 5, 2, 2, 21, 14, 2, 2, 1, 18, 43, 13, 7, 7, 6],
    [5, 1, 4, 0, 1, 2, 3, 8, 27, 9, 2, 2, 11, 7, 1, 11, 17, 5, 1, 4],
    [11, 0, 4, 6, 1, 4, 0, 13, 30, 10, 29, 4, 1, 11, 22, 4, 38, 18, 11, 8],
    [13, 18, 9, 8, 5, 2, 11, 13, 37, 3, 1, 4, 10, 14, 16, 4, 15, 20, 6, 6],
    [41, 10, 2, 0, 21, 1, 4, 5, 3, 17, 19, 7, 4, 18, 5, 0, 5, 9, 17, 3],
    [16, 16, 1, 1, 0, 2, 0, 24, 1, 5, 28, 17, 7, 0, 22, 16, 7, 4, 2, 10],
]

# Derived data.
inbound_truck_count = len(_inbound_truck_raw_data)
outbound_truck_count = len(_outbound_truck_raw_data)
total_truck_count = inbound_truck_count + outbound_truck_count