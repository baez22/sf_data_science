"""Game 'Guess the number'
Computer plays the game by itself
"""

import numpy as np

def random_predict(number:int=1) -> int:
    count = 0
    
    while True:
        count += 1
        predict_number = np.random.randint(1,101)
        if number == predict_number:
            break
    return(count)


def score_game(random_predict) -> int:
    """Average number of tries for def for finding a number

    Args:
        random_predict (_type_): function finds the number

    Returns:
        int: average number of tries
    """
    
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1,101, size = 1000)
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls))
    print(f"Your programm finds the number in average for {score} tries")
    return(score)

if __name__ == "__main__":
    score_game(random_predict)

