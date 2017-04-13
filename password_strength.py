import os
from getpass import getpass

os.chdir(os.path.dirname(os.path.abspath(__file__)))


SCORE_BLACK_LIST = 1
SCORE_DIGIT = 1
SCORE_LOWERCASE_AND_UPPERCASE = 2
SCORE_SPECIAL_CHAR = 2
SCORE_LENGTH = 4

def get_score_black_list(password):
    score = 0
    with open('data/black_list.txt') as f:
        black_list = map(lambda item: item.strip(), f.readlines())
        if all(password != item for item in black_list): 
            score = SCORE_BLACK_LIST
            
    return score

def get_score_digit(password):
    score = 0
    if any(char.isdigit() for char in password): 
        score = SCORE_DIGIT
    return score

def get_score_lowercase_and_uppercase(password):
    score = 0
    if any( char.isupper() for char in password) and \
       any(char.islower() for char in password): 
        score = SCORE_LOWERCASE_AND_UPPERCASE
    return score


def get_score_special_char(password):
    score = 0
    special_characters = '!@#$%^&*()_+.,:;'
    if any(char in special_characters for char in password): 
        score = SCORE_SPECIAL_CHAR
    return score


def get_score_length(password):
    score = 0
    if len(password) >= 12:
        score = SCORE_LENGTH
    return score

def get_password_strength(password):
    score = 0
    if not password: # Если пароль пуст 0 баллов
        return score

    score += get_score_black_list(password)
    score += get_score_digit(password)
    score += get_score_lowercase_and_uppercase(password)
    score += get_score_special_char(password)
    score += get_score_length(password)

    return score


if __name__ == '__main__':
    print('Программа. Сложность пароля.\n')
    answer = getpass(prompt='Введите пароль: ')
    password_strength = get_password_strength(answer)
    print('Оценка сложности Вашего пароля: {}'.format(password_strength))
