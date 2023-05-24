class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __mul__(self, other):
        real_part = self.real * other.real - self.imaginary * other.imaginary
        imaginary_part = self.real * other.imaginary + self.imaginary * other.real
        return ComplexNumber(real_part, imaginary_part)

    def display(self):
        if self.imaginary < 0:
            operator = "-"
        else:
            operator = "+"
        print(f"{self.real} {operator} {abs(self.imaginary)}i")


# Creating complex numbers
c1 = ComplexNumber(3, 2)
c2 = ComplexNumber(1, -4)

# Multiplying two complex numbers
result = c1 * c2

# Displaying the result
result.display()
