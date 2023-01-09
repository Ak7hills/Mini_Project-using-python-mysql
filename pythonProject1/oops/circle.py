class Circle:
    def __init__(self, a, b, r):
        self.a = a
        self.b = b
        self.r = r

    def perimeter(self):
        return 2 * 3.14* self.r

    def area(self):
        return 3.14 * self.r ** 2

    # form of the circle equation
    def formEquation(self, x, y):
        return (x - self.a) ** 2 + (y - self.b) ** 2 - self.r ** 2

    # method to test if given point belong to the circle or not
    def test_belong(self, x, y):
        if (self.formEquation(x, y) == 0):
            print("the point: (", x, y, ") belongs to the circle C")
        else:
            print("the point: (", x, y, ") does not belong to the circle C")


# Creating of an instance object
C = Circle(2, 2, 3)

print("the perimeter of the circle C is:", C.perimeter())
print("the area of circle C is:", C.area())
# we test if the point(1,1) belong to the circle or not
C.test_belong(1, 1)