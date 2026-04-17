import math


def degree_to_radian(degree):
    # Convert degree to radian
    return degree * (math.pi / 180)


def area_of_trapezoid(height, base1, base2):
    # Calculate trapezoid area
    return (base1 + base2) * height / 2


def area_of_regular_polygon(num_sides, side_length):
    # Calculate regular polygon area
    return (num_sides * side_length * side_length) / (4 * math.tan(math.pi / num_sides))


def area_of_parallelogram(base, height):
    # Calculate parallelogram area
    return base * height


if __name__ == "__main__":
    degree = float(input("Input degree: "))
    print(f"Output radian: {degree_to_radian(degree):.6f}")

    height = float(input("Height: "))
    base1 = float(input("Base1: "))
    base2 = float(input("Base2: "))
    print(f"Output: {area_of_trapezoid(height, base1, base2)}")

    num_sides = int(input("Input number of sides: "))
    side_length = float(input("Input side length: "))
    print(f"Output: {area_of_regular_polygon(num_sides, side_length):.0f}")

    base = float(input("Base: "))
    h = float(input("Height: "))
    print(f"Output: {area_of_parallelogram(base, h):.1f}")