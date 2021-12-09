# PROJECT: (WK-02) Cuboid
# Solution written by Darren Halpin

width = int(input("Enter the cuboid width: "))
length = int(input("Enter the cuboid length: "))
height = int(input("Enter the cuboid height: "))

surface_area = ((length * width) * 2) + \
               ((length * height) * 2) + \
               ((height * width) * 2)

cuboid_volume = height * width * length

print("The surface area of the cuboid is " + str(surface_area))
print("The volume of the cuboid is " + str(cuboid_volume))


