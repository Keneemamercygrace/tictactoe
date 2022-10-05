import random
import time


def get_winner(win_list, moves):
    if win_list[0] == 'O' and win_list[2] == 'O' and win_list[4] == 'O':
        print("computer wins")
        return True
    elif win_list[0] == 'X' and win_list[2] == 'X' and win_list[4] == 'X':
        print("You win! Congratulations")
        return True
    elif win_list[13] == 'O' and win_list[15] == 'O' and win_list[17] == 'O':
        print("You Lose! Computer Wins")
        return True
    elif win_list[13] == 'X' and win_list[15] == 'X' and win_list[17] == 'X':
        print("You win! Congratulations")
        return True
    elif win_list[26] == 'O' and win_list[28] == 'O' and win_list[30] == 'O':
        print("You Lose! Computer Wins")
        return True
    elif win_list[26] == 'X' and win_list[28] == 'X' and win_list[30] == 'X':
        print("You win! Congratulations")
        return True
    elif win_list[26] == 'O' and win_list[15] == 'O' and win_list[4] == 'O':
        print("You Lose! Computer Wins")
        return True
    elif win_list[26] == 'X' and win_list[15] == 'X' and win_list[4] == 'X':
        print("You win! Congratulations")
        return True
    elif win_list[0] == 'O' and win_list[15] == 'O' and win_list[30] == 'O':
        print("You Lose! Computer Wins")
        return True
    elif win_list[0] == 'X' and win_list[15] == 'X' and win_list[30] == 'X':
        print("You win! Congratulations")
        return True
    elif win_list[0] == 'O' and win_list[13] == 'O' and win_list[26] == 'O':
        print("You Lose! Computer Wins")
        return True
    elif win_list[0] == 'X' and win_list[13] == 'X' and win_list[26] == 'X':
        print("You win! Congratulations")
        return True
    elif win_list[2] == 'O' and win_list[15] == 'O' and win_list[28] == 'O':
        print("You Lose! Computer Wins")
        return True
    elif win_list[2] == 'X' and win_list[15] == 'X' and win_list[28] == 'X':
        print("You win! Congratulations")
        return True
    elif win_list[4] == 'O' and win_list[17] == 'O' and win_list[30] == 'O':
        print("You Lose! Computer Wins")
        return True
    elif win_list[4] == 'X' and win_list[17] == 'X' and win_list[30] == 'X':
        print("You win! Congratulations")
        return True


print("Welcome to the tic tac toe game")
print('O|X|O \n------\nO|X|X\n------\nX|O|O')
game = '1|2|3\n------\n4|5|6\n------\n7|8|9'
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# win_list = []
n = len(nums)
still_playing = True

while n > 0:
    n -= 1
    computer = str(random.choice(nums))
    print(computer)
    if len(nums) == 1:
        comp_round = game.replace(computer, 'O')
        computer = int(computer)
        nums.remove(computer)
        game = comp_round
        print(game)
        print('It\'s a draw')
        break
    user = input(f"The computer will play noughts and you will play crosses \n"
                 f" To select your desired position, type the number in that position\n{game}\n")
    new = game.replace(user, 'X')
    user = int(user)
    nums.remove(user)
    comp_round = new.replace(computer, 'O')
    computer = int(computer)
    nums.remove(computer)
    game = comp_round
    print(game)
    if get_winner(game, nums):
        break
    time.sleep(4)
    if n == 0:
        break

