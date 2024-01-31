import random

def select_random_car_brand():
    car_brands = ["Toyota", "Ford", "Honda", "Chevrolet", "BMW"]
    random_brand = random.choice(car_brands)
    return random_brand

if __name__ == "__main__":
    random_car_brand = select_random_car_brand()
    print("Randomly selected car brand:", random_car_brand)
