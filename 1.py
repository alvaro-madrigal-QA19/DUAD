class Circle:
    pi = 3.1416

    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        result = 3.1416 * (self.radius ** 2)
        return result

circle = float(input('Enter measurement of the circle: '))
calculate = Circle(circle)

print('area: ', calculate.get_area())