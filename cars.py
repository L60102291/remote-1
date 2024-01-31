import random

def select_random_model_year():
    return random.randint(1990, 2023)

if __name__ == "__main__":
    random_model_year = select_random_model_year()
    print("Randomly selected model year:", random_model_year)
