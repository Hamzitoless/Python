class vehicle:#Class is the blueprint of objects
    def __init__(self,make,model):
        self.make=make
        self.model=model

    def moves(self):
        print("The car is moving")

    def get_make_model(self):
        print(f"The car is a {self.make} {self.model}")    

my_car=vehicle("Toyota","Supra")#Declaring an object
my_car.get_make_model()
my_car.moves()       

your_car=vehicle("Lamborghini","Urus")
your_car.get_make_model()
your_car.moves()       