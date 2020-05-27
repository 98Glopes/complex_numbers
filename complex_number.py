import math

class ComplexNumber():
    """
    Class to implement complex  number representation in python
    mode argument must be "rec" to rectangulor mode or "pol" to polar mode
    in rec mode: "a" is the real component and "b" is the imaginary component
    in pol mode: "a" is the absolute value of vector and "b" is the vector angle
    the pashe angle is printed in deegres
    """
    def __init__(self, mode, a, b):

        self.mode = mode
        if self.mode == 'rec':

            self.real = a
            self.imag = b
            self._to_polar()
        
        elif self.mode == 'pol':

            self.abs = a
            self.phase = math.radians(b)
            self._to_rec()
    
    def _to_polar(self):

        self.abs = math.sqrt(self.real**2 + self.imag**2)
        self.phase = math.atan2(self.imag, self.real)

    def _to_rec(self):

        self.real = self.abs*math.cos(self.phase)
        self.imag = self.abs*math.sin(self.phase)

    def __str__(self):

        if self.mode == 'rec':
            return "%.2f + %.2fi" % (self.real, self.imag)
        elif self.mode == 'pol':
            return "%.2f < %.2f°" % (self.abs, math.degrees(self.phase))

    def __add__(self, other):
        a = self.real + other.real
        b = self.imag + other.imag
        return ComplexNumber('rec', a, b)

    def __sub__(self, other):
        a = self.real - other.real
        b = self.imag - other.imag
        return ComplexNumber('rec', a, b)

    def __mul__(self, other):
        a = self.abs * other.abs 
        b = self.phase + other.phase
        return ComplexNumber('pol', a, b)
        
    def __div__(self, other):
        a = self.abs / other.abs
        b = self.phase - other.phase
        return ComplexNumber('pol', a, b)
