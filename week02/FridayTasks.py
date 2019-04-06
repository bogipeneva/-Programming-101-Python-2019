import sys


def hangman(clue_word):
    current_tries = 0

    print("Welcome to Hangman! Let's play!")
    
    current_word = []
    for elem in clue_word:
        current_word.append('_')
        

    print(' '.join(current_word))
    
    list_clue_word = [x for x in clue_word]
    temp = []
    

    while current_word != list_clue_word and current_tries < 11:

        print("Guess a letter: ")

        temp = [x for x in current_word]

        letter = input()

        for index in range(len(list_clue_word)):
            if list_clue_word[index] == letter:
                current_word[index] = letter

        if temp == current_word:
            print("Incorrect!")
            current_tries += 1
        else:
            print(' '.join(current_word))
            current_tries += 1


    if current_word == list_clue_word:
        print("Congratulations!")
    else:
        print(" _____")
        print("|  |  |")
        print("| \o/ |")
        print("|  |  |")
        print("|  |  |")
        print("| / \ |")

from copy import deepcopy
import collections

def matrix_bombing_plan(m):

    rows = len(m)
    cols = len(m[0])
    dictionary_bombing_plan = {}
    val = 0
    

    for row in range(rows):
        for col in range(cols):
            temp_matrix = deepcopy(m)


            if row == col == 0:
                temp_matrix[row][col + 1] = temp_matrix[row][col + 1] - temp_matrix[row][col] if temp_matrix[row][col + 1] >= m[row][col] else 0
                temp_matrix[row + 1][col + 1] = temp_matrix[row + 1][col + 1] - temp_matrix[row][col] if temp_matrix[row + 1][col + 1] >= m[row][col] else 0
                temp_matrix[row + 1][col] = temp_matrix[row + 1][col] - temp_matrix[row][col] if temp_matrix[row + 1][col] >= m[row][col] else 0
                val = sum([sum(x) for x in temp_matrix])
                dictionary_bombing_plan.update({(row,col): val})
                val = 0


            elif row == 0  and col < cols - 1:
                temp_matrix[row][col + 1] = temp_matrix[row][col + 1] - temp_matrix[row][col] if temp_matrix[row][col + 1] >= m[row][col] else 0
                temp_matrix[row + 1][col + 1] = temp_matrix[row + 1][col + 1] - temp_matrix[row][col] if temp_matrix[row + 1][col + 1] >= m[row][col] else 0
                temp_matrix[row + 1][col] = temp_matrix[row + 1][col] - temp_matrix[row][col] if temp_matrix[row + 1][col] >= m[row][col] else 0
                temp_matrix[row + 1][col - 1] = temp_matrix[row + 1][col - 1] - temp_matrix[row][col] if temp_matrix[row + 1][col - 1] >= m[row][col] else 0
                temp_matrix[row][col - 1] = temp_matrix[row][col - 1] - temp_matrix[row][col] if temp_matrix[row][col - 1] >= m[row][col] else 0

                val = sum([sum(x) for x in temp_matrix])
                dictionary_bombing_plan.update({(row,col): val})
                val = 0

            elif row == 0 and col == cols - 1:
                temp_matrix[row][col - 1] = temp_matrix[row][col - 1] - temp_matrix[row][col] if temp_matrix[row][col - 1] >= m[row][col] else 0
                temp_matrix[row + 1][col - 1] = temp_matrix[row + 1][col - 1] - temp_matrix[row][col] if temp_matrix[row + 1][col - 1] >= m[row][col] else 0
                temp_matrix[row + 1][col] = temp_matrix[row + 1][col] - temp_matrix[row][col] if temp_matrix[row + 1][col] >= m[row][col] else 0
                val = sum([sum(x) for x in temp_matrix])
                dictionary_bombing_plan.update({(row,col): val})
                val = 0

            elif row < rows -1 and col == 0:
                temp_matrix[row][col + 1] = temp_matrix[row][col + 1] - temp_matrix[row][col] if temp_matrix[row][col + 1] >= m[row][col] else 0
                temp_matrix[row + 1][col + 1] = temp_matrix[row + 1][col + 1] - temp_matrix[row][col] if temp_matrix[row + 1][col + 1] >= m[row][col] else 0
                temp_matrix[row + 1][col] = temp_matrix[row + 1][col] - temp_matrix[row][col] if temp_matrix[row + 1][col] >= m[row][col] else 0
                temp_matrix[row - 1][col + 1] = temp_matrix[row - 1][col + 1] - temp_matrix[row][col] if temp_matrix[row - 1][col + 1] >= m[row][col] else 0
                temp_matrix[row - 1][col] = temp_matrix[row - 1][col] - temp_matrix[row][col] if temp_matrix[row - 1][col] >= m[row][col] else 0
                val = sum([sum(x) for x in temp_matrix])
                dictionary_bombing_plan.update({(row,col): val})
                val = 0

            elif row == rows - 1 and col == 0:
                temp_matrix[row][col + 1] = temp_matrix[row][col + 1] - temp_matrix[row][col] if temp_matrix[row][col + 1] >= m[row][col] else 0
                temp_matrix[row - 1][col + 1] = temp_matrix[row - 1][col + 1] - temp_matrix[row][col] if temp_matrix[row - 1][col + 1] >= m[row][col] else 0
                temp_matrix[row - 1][col] = temp_matrix[row - 1][col] - temp_matrix[row][col] if temp_matrix[row - 1][col] >= m[row][col] else 0
                val = sum([sum(x) for x in temp_matrix])
                dictionary_bombing_plan.update({(row,col): val})
                val = 0

            elif row == rows -1  and col < cols - 1:
                temp_matrix[row][col + 1] = temp_matrix[row][col + 1] - temp_matrix[row][col] if temp_matrix[row][col + 1] >= m[row][col] else 0
                temp_matrix[row - 1][col - 1] = temp_matrix[row - 1][col - 1] - temp_matrix[row][col] if temp_matrix[row - 1][col - 1] >= m[row][col] else 0
                temp_matrix[row - 1][col] = temp_matrix[row - 1][col] - temp_matrix[row][col] if temp_matrix[row - 1][col] >= m[row][col] else 0
                temp_matrix[row - 1][col + 1] = temp_matrix[row - 1][col + 1] - temp_matrix[row][col] if temp_matrix[row - 1][col + 1] >= m[row][col] else 0
                temp_matrix[row][col - 1] = temp_matrix[row][col - 1] - temp_matrix[row][col] if temp_matrix[row][col - 1] >= m[row][col] else 0
                val = sum([sum(x) for x in temp_matrix])
                dictionary_bombing_plan.update({(row,col): val})
                val = 0

            elif row == rows - 1 and col == cols - 1:
                temp_matrix[row][col - 1] = temp_matrix[row][col - 1] - temp_matrix[row][col] if temp_matrix[row][col - 1] >= m[row][col] else 0
                temp_matrix[row - 1][col - 1] = temp_matrix[row - 1][col - 1] - temp_matrix[row][col] if temp_matrix[row - 1][col - 1] >= m[row][col] else 0
                temp_matrix[row - 1][col] = temp_matrix[row - 1][col] - temp_matrix[row][col] if temp_matrix[row - 1][col] >= m[row][col] else 0
                val = sum([sum(x) for x in temp_matrix])
                dictionary_bombing_plan.update({(row,col): val})
                val = 0

            elif row < rows -1 and col == cols - 1:
                temp_matrix[row][col - 1] = temp_matrix[row][col - 1] - temp_matrix[row][col] if temp_matrix[row][col - 1] >= m[row][col] else 0
                temp_matrix[row + 1][col - 1] = temp_matrix[row + 1][col - 1] - temp_matrix[row][col] if temp_matrix[row + 1][col - 1] >= m[row][col] else 0
                temp_matrix[row + 1][col] = temp_matrix[row + 1][col] - temp_matrix[row][col] if temp_matrix[row + 1][col] >= m[row][col] else 0
                temp_matrix[row - 1][col - 1] = temp_matrix[row - 1][col - 1] - temp_matrix[row][col] if temp_matrix[row - 1][col - 1] >= m[row][col] else 0
                temp_matrix[row - 1][col] = temp_matrix[row - 1][col] - temp_matrix[row][col] if temp_matrix[row - 1][col] >= m[row][col] else 0
                val = sum([sum(x) for x in temp_matrix])
                dictionary_bombing_plan.update({(row,col): val})
                val = 0

            else:
                temp_matrix[row - 1][col - 1] = temp_matrix[row - 1][col - 1] - temp_matrix[row][col] if temp_matrix[row - 1][col - 1] >= m[row][col] else 0
                temp_matrix[row - 1][col] = temp_matrix[row - 1][col] - temp_matrix[row][col] if temp_matrix[row - 1][col] >= m[row][col] else 0
                temp_matrix[row - 1][col + 1] = temp_matrix[row - 1][col + 1] - temp_matrix[row][col] if temp_matrix[row - 1][col + 1] >= m[row][col] else 0
                temp_matrix[row][col - 1] = temp_matrix[row][col - 1] - temp_matrix[row][col] if temp_matrix[row][col - 1] >= m[row][col] else 0
                temp_matrix[row][col + 1] = temp_matrix[row][col + 1] - temp_matrix[row][col] if temp_matrix[row][col + 1] >= m[row][col] else 0
                temp_matrix[row + 1][col - 1] = temp_matrix[row + 1][col - 1] - temp_matrix[row][col] if temp_matrix[row + 1][col - 1] >= m[row][col] else 0
                temp_matrix[row + 1][col] = temp_matrix[row + 1][col] - temp_matrix[row][col] if temp_matrix[row + 1][col] >= m[row][col] else 0
                temp_matrix[row + 1][col + 1] = temp_matrix[row + 1][col + 1] - temp_matrix[row][col] if temp_matrix[row + 1][col + 1] >= m[row][col] else 0

                val = sum([sum(x) for x in temp_matrix])
                dictionary_bombing_plan.update({(row,col): val})
                val = 0
    return dictionary_bombing_plan





def main():
    print(matrix_bombing_plan([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))


if __name__ == '__main__':
    main()