import math


def main():
    area = circle_area(100)
    print(f'The area of the circle is {area:<.3f} square units.')

def circle_area(radius):
    return math.pi * radius ** 2

if __name__ == '__main__':
    main()