# PROJECT: (WK-01) Cans of paint
# Solution written by Darren Halpin

import math

# define constants
c_paint_can_coverage = float(5.1)
c_paint_can_diameter = float(0.15)
c_paint_can_height = float(0.3)

c_box_length = float(0.6)
c_box_width = float(0.3)
c_box_height = float(0.35)

c_hall_x = int(40)
c_hall_y = int(30)
c_hall_height = float(3.4)

# calculate total area of hall
sqm_hall_wall_1 = (c_hall_x * c_hall_height) * 2
sqm_hall_wall_2 = (c_hall_y * c_hall_height) * 2
sqm_hall_total = sqm_hall_wall_1 + sqm_hall_wall_2

# calculate total number of tins required
number_of_cans = math.ceil(sqm_hall_total / c_paint_can_coverage)

# calculate qty of tins per box
box_qty_x = math.floor(c_box_length / c_paint_can_diameter)
box_qty_y = math.floor(c_box_width / c_paint_can_diameter)
box_qty_height = math.floor(c_box_height / c_paint_can_height)
cans_per_box = (box_qty_y * box_qty_x) * box_qty_height

# calculate number of boxes and excess tins
get_boxes = math.modf(number_of_cans / cans_per_box)
full_boxes = int(get_boxes[1])
extra_cans = math.ceil(get_boxes[0] * cans_per_box)

# output information
print("Number of cans required: " + str(number_of_cans))
print("Number of cans in box: " + str(cans_per_box))
print("Number of full boxes: " + str(full_boxes))
print("Cans not packed in boxes: " + str(extra_cans))

