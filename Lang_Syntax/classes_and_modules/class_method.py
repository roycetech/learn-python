 #!/usr/bin/env python


# Static Method, omitting the self parameter makes them so.
class Math:
    def square(n):
        return n ** 2


class Square:
  def draw(self):
    print("Drawing a square")
    

print( Math.square( 5 ) )
Square().draw()



class Mom:
    pass


class Dad:
    pass


class Son(Mom, Dad):
    pass
