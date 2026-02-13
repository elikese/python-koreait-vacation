class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_me(self):
        print(f"[{self.name}] {self.age}살")