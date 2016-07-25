
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def draw(self):
        print("Drawing rectangle of width {} and height {}" \
            .format(self.width, self.height))

    def static():
        print("Static Method")


Rectangle.static()

rect1 = Rectangle(1, 2)
rect1.draw()

rect2 = Rectangle(10, 5)

print('rect.width: %d' % rect1.width)
print('rect.height: %d' % rect1.height)


# Demo use of class variable
count = 0
class Counter(object):
    def show():
        print(count)



counter1 = Counter()
counter2 = Counter()

Counter.show()



