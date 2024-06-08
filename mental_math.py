import time
import random

from store_results import update_csv

def input_valid(input):
    if len(input) == 0:
        return False
    
    if input[0] == '-':
        input = input[1:]

    if len(input) == 0:
        return False
    
    if input.isdigit():
        return True
    return False

def run_game(game_mode='standard'):
    t_end = time.time() + 60 * 2
    correct, false = 0, 0
    while time.time() < t_end:
        
        if game_mode=='standard':
            mode = random.randint(0, 3)

            if mode < 2:
                a = random.randint(1, 100)
                b = random.randint(1, 100)
            elif mode == 2:
                a = random.randint(2, 100)
                b = random.randint(2, 12)
            else:
                a = random.randint(2, 12)
                b = random.randint(2, 12)
                a = a*b

        elif game_mode=='large_multi':
            mode = 2
            a = random.randint(13, 100)
            b = random.randint(13, 100)

        elif game_mode =='complex':
            mode = random.randint(0, 9)
            if 1 <= mode <= 2:
                mode = 1
            elif 3 <= mode <= 7:
                mode = 2
            else:
                mode = 3

            if mode < 2:
                a = random.randint(101, 1000)
                b = random.randint(101, 1000)
            elif mode == 2:
                a = random.randint(13, 100)
                b = random.randint(13, 100)
            else:
                a = random.randint(13, 100)
                b = random.randint(2, 12)
                a = a*b

        operations = {0: '+', 1: '-', 2: 'x', 3: '/'}

        if mode == 0:
            key = a + b
        elif mode == 1:
            key = a - b
        elif mode == 2:
            key = a*b
        elif mode == 3:
            key = a//b

        ans = input(f'{a} {operations[mode]} {b} = :')

        while not input_valid(ans) or int(ans) != key:
            if input_valid(ans):
                false += 1
            ans = input(f'{a} {operations[mode]} {b} = :')
            
        
        correct += 1

    if not update_csv(correct, false, game_mode):
        print('Error!')

    print(f'Correct answers: {correct}\n')
    print(f'Accuracy: {correct/(correct+false)}')
        
if __name__ == "__main__":
    run_game('complex')

