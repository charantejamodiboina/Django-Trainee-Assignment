# Task: Create a Rectangle class with iteration capabilities

class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        yield {'length': self.length}
        yield {'width': self.width}


rectangle = Rectangle(10, 5)

# Iterating over the rectangle object
for attribute in rectangle:
    print(attribute)