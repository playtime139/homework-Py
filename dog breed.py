class Dog:
    species = "dog"

    def __init__(self, breed, age, name):
        self.breed = breed
        self.age = age
        self.name = name

    def display_details(self):
        print(self.name ," is a", Dog.species)
        print("his breed is a ", self.breed)
        print("he is ", self.age, "years old")
        print("--------------------")


tom = Dog("German Shepherd", 5, "tom")
jerry = Dog("Golden Retriever", 3, "jerry")

tom.display_details()
jerry.display_details()
