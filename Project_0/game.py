import numpy as np
number = np.random.randint(1, 101)
count = 0

while True:
    count += 1
    predict_number = int(input("Guess the number from 1 to 100 "))
    
    if predict_number > number:
        print("The number has to be less!")
    elif predict_number < number:
        print("The number has to be bigger!")
    else: 
        print(f"Yes! You found the number {number} by {count} tries!")
        break
    
