import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def check_black_list(password):
    '''
    Если пароля нет в blacklist вернуть значение 1
    иначе 0
    '''
    score = 0
    f = open('data/black_list.txt')
    black_list = map(lambda item: item.strip(), f.readlines())
    f.close()
    
    if all(password != item for item in black_list): 
        score = 1
    return score

def check_digit(password):
    '''
    Если есть цифра в пароле вернуть 1
    иначе 0
    '''
    score = 0
    if any(char.isdigit() for char in password): 
        score = 1
    return score

def check_lower_and_upper(password):
    '''
    Если есть нижний и верхний регистр вернуть 2
    иначе 0
    '''
    score = 0
    if any( char.isupper() for char in password) and \
       any(char.islower() for char in password): 
        score =  2
    return score


def check_special_char(password):
    '''
    Если есть спец символ, то вернуть 2
    иначе 0
    '''
    score = 0
    special_characters = '!@#$%^&*()_+.,:;'
    if any(char in special_characters for char in password): 
        score = 2
    return score


def check_length(password):
    '''
    Если длина пароля от 12 вернуть 4
    иначе 0
    '''
    score = 0
    if len(password) >= 12:
        score = 4
    return score

def get_password_strength(password):
    score = 0
    if len(password) == 0: # Если пароль пуст 0 баллов
        return score

    score += check_black_list(password)
    score += check_digit(password)
    score += check_lower_and_upper(password)
    score += check_special_char(password)
    score += check_length(password)

    return score




if __name__ == '__main__':
    print('Программа. Сложность пароля.\n')
    answer = input('Введите пароль: ')
    password_strength = get_password_strength(answer)
    print('Оценка сложности Вашего пароля: {}'.format(password_strength))
