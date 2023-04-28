
measurement_type = input("Enter measurement type (radius or diameter): ")
if measurement_type.lower() == "radius":
    radius = float(input("Enter radius: "))
    diameter = radius * 2
elif measurement_type.lower() == "diameter":
    diameter = float(input("Enter diameter: "))
    radius = diameter / 2
else:
    print("Invalid measurement type!")
    exit()


pi = 3.14159
area = pi * radius ** 2
perimeter = 2 * pi * radius


print(f"Area: {area:.2f}")
print(f"Perimeter: {perimeter:.2f}")
