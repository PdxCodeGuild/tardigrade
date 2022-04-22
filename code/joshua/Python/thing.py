class Animal:
  def __init__(self, legs, color):
    self.legs = legs
    self.color = color
  def make_sound(self):
    print(f"I am a {self.legs} legged {self.color } animal!")


class Rabbit(Animal):
    def __init__(self, legs, color, speed): ##adding the new attribute speed
        # super().__init__(legs, color) ## referencing old attributes legs,color
        self.speed = speed
    def test():
        return "hello"

elephant = Animal("4", "grey")
rabbit = Rabbit("2", "white", 10) ## 'Rabbit' object has no attribute 'legs'
rabbit.make_sound()



