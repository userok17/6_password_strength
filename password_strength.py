import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def get_password_strength(password):
    score = 0
    if len(password) == 0: # Если пароль пуст 0 баллов
        return score

    f = open('data/black_list.txt')
    black_list = map(lambda item: item.strip(), f.readlines())
    f.close()

    if all(password != item for item in black_list): # Если пароля нет в blacklist +1
        score += 1
    
    if any(char.isdigit() for char in password): # Если есть цифра +1
        score += 1

    if any( char.isupper() for char in password) and \
       any(char.islower() for char in password): # Если есть нижний и верхний регистр +1
        score += 2
    
    special_characters = '!@#$%^&*()_+.,:;'
    if any(char in special_characters for char in password): # Если есть спец символы +2
        score += 2

    if len(password) >= 12: # Если длина пароля от 12 символов +4
        score += 4

    return score


if __name__ == '__main__':
    print('Программа. Сложность пароля.\n')
    answer = input('Введите пароль и получите оценку от 1 до 10: ')
    password_strength = get_password_strength(answer)
    print('Оценка сложности Вашего пароля: {}'.format(password_strength))
