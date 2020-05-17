class Live:
    def __init__(self, name, age, sex, height, weight):
        self.name = name
        self.age = age
        self.sex = sex
        self.height = height
        self.weight = weight

    def drinkwater(self):
        print("drinkwater")

    def eat(self):
        print("eat")

    def sleep(self):
        print("sleep")

    @staticmethod
    def bath():
        print("bath")


lives = Live("袁锋", "35", "男", "176cm", "80kg")
lives.drinkwater()
Live.bath()

