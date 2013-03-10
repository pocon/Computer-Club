class Car:
    def __init__(self, etag, numberplate):
        self.etag = etag
        self.numberplate = numberplate
        self.crossed = 0

    def cross(self):
        self.crossed += 1


# Testing Code:

c = Car(etag="12445", numberplate = "ABC123")

c.cross()

print "Car has crossed", c.crossed, "times"
