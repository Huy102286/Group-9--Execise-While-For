x_coords = []
y_coords = []

print("Enter the x part of the coordinate (blank to quit):")
x_input = input("Enter the x part of the coordinate: ")

while x_input != "":
    y_input = input("Enter the y part of the coordinate: ")
    x_coords.append(float(x_input))
    y_coords.append(float(y_input))
    x_input = input("Enter the x part of the coordinate (blank to quit): ")

perimeter = 0
n = len(x_coords)

for i in range(n):
    if i < n - 1:
        distance = ((x_coords[i] - x_coords[i+1])**2 + (y_coords[i] - y_coords[i+1])**2)**0.5
        perimeter += distance
    else:
        distance = ((x_coords[i] - x_coords[0])**2 + (y_coords[i] - y_coords[0])**2)**0.5
        perimeter += distance

print("The perimeter of that polygon is", perimeter)