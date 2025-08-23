from math import exp, sqrt, cos, sin


class ComplexNumber(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return  ComplexNumber((self.real + other.real), (self.imaginary + other.imaginary))

    def __mul__(self, other):
        real = (self.real * other.real) - (self.imaginary * other.imaginary)
        imaginary = (self.imaginary * other.real) + (self.real * other.imaginary)
        return ComplexNumber(real, imaginary)

    def __sub__(self, other):
        return  ComplexNumber((self.real - other.real), (self.imaginary - other.imaginary))

    def __truediv__(self, other):
        real = (self.real * other.real + self.imaginary * other.imaginary) / (other.real ** 2 + other.imaginary ** 2)
        imaginary = (self.imaginary * other.real - self.real * other.imaginary) / (other.real ** 2 + other.imaginary ** 2)
        return ComplexNumber(real, imaginary)
    
    def __eq__(self, other):
        if isinstance(other, ComplexNumber):
            return self.real == other.real and self.imaginary == other.imaginary
        return False

    def __abs__(self):
        return sqrt(self.real ** 2 + self.imaginary ** 2)

    def conjugate(self):
        return ComplexNumber(self.real, (self.imaginary * -1))

    def exp(self):
        real = exp(self.real) * cos(self.imaginary)
        imaginary = exp(self.real) * sin(self.imaginary)
        return ComplexNumber(real, imaginary)
